import socket
import threading
import traceback
import queue
import pickle

class MessageCenter(threading.Thread):
    def __init__(self, max_cons, sv_port, sv_id=None, sv_host=None):
        threading.Thread.__init__(self, daemon=True)

        self._qMessageQueue = queue.Queue()
        self.debug = True
        self.debug_msg = []
        self.max_cons = int(max_cons)
        self._sLocalHostPort = int(sv_port)
        self._sLocalHostIP = sv_host
        if sv_id:
            self._sLocalHostName = sv_id
        else:
            self._sLocalHostName = '{}:{}'.format(sv_host, sv_port)

        self.con_list = {}
        # use to shutdown server.
        self.shutdown = False

    def run(self):
        s = self.makeserversocket()
        # set connection timeout for 2 seconds.
        # s.settimeout(5)
        self.__debug('Server start: {} {}:{}'.format(self._sLocalHostName, self._sLocalHostIP, self._sLocalHostPort))

        while not self.shutdown:
            try:
                # when new connection is coming.
                clt_sock, clt_addr = s.accept()
                self.__debug('A new connection coming...')
                clt_sock.settimeout(None)

                # make a thread to let it handle the msg.
                t = threading.Thread(target=self.__handleconnection, args=[clt_sock])
                self.__debug('Start a new thread')
                t.daemon = True
                t.start()
            except KeyboardInterrupt:
                self.shutdown = True
                continue
            except:
                if self.debug:
                    traceback.print_exc()
                continue

        self.__debug('Main loop exiting...')
        s.close()

    def makeserversocket(self, backlog=5):
        # specify the connection type, here is (use internet, TCP connection).
        s = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
        # set the socket port can be reused.
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # prepare the socket and port.
        s.bind((self._sLocalHostIP, self._sLocalHostPort))
        # start listening the socket and allow the 'backlog' number of connection.
        s.listen(backlog)
        return s

    def __handleconnection(self, clientsocket):
        # get the ip and port number of client(peer) side .
        host, port = clientsocket.getpeername()
        # create a message center to receive and reply to the connection.
        msgconn = ConnectionPort(None, host, port, clientsocket)
        try:
            newmsg = msgconn.recv_data()
            msgconn.send_data('ACK', 'I know you are good.')
            self.__debug('{} receive msg: {}'.format(self._sLocalHostName, newmsg))
        except :
            if self.debug:
                traceback.print_exc()
        # saving msg.
        self._qMessageQueue.put(newmsg)

        self.__debug('{} now have :'.format(self._sLocalHostName))
        print(list(self._qMessageQueue.queue))

        self.__debug('Disconnecting' + str(clientsocket.getpeername()))
        msgconn.close()

    def getNewMessage(self):
        # pop msg once a time.
        return self._qMessageQueue.get()

    def sendNewMessage(self, host, port, msgtype, msgdata, pid=None ):
        # send msg to a host and get its reply.
        msgreply = []
        try:
            # make connection to the the server side.
            if pid == None:
                pid = self._sLocalHostName
            msgconn = ConnectionPort(pid, host, port)
            msgconn.send_data(msgtype, msgdata)
            self.__debug('{} sent: {}'.format(pid, msgdata))

            replymsg = msgconn.recv_data()
            while replymsg != None:
                msgreply.append(replymsg)
                self.__debug('{} got reply: {}'.format(pid, str(msgreply)))
                replymsg = msgconn.recv_data()
        except KeyboardInterrupt:
            raise
        except:
            if self.debug:
                traceback.print_exc()

        return msgreply

    def __debug(self, msg):
        self.debug_msg.append(msg)
        if self.debug:
            print(msg)


class ConnectionPort():
    def __init__(self, pid, host, port, sock=None):
        self.debug = True
        if not sock:
            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.s.connect((host, int(port)))
        else:
            self.s = sock
        
        # self.sockdata = self.s.makefile('rw', 0)

    def __makemsg(self, msgtype, msgdata):
        # make the data into pickle format.
        msg_data = [msgtype, msgdata]
        msg = pickle.dumps(msg_data)
        return msg

    def __readmsg(self, recvmsg):
        msg = pickle.loads(recvmsg)
        return msg

    def recv_data(self):
        try:
            msg = self.__readmsg(self.s.recv(4096))
        except KeyboardInterrupt:
            raise
        except EOFError:
            # out of msg
            return None
        except :
            if self.debug:
                traceback.print_exc()
            return None
        return msg
            
    def send_data(self, msgtype, msgdata):
        try:
            msg = self.__makemsg(msgtype, msgdata)
            self.s.send(msg)
        except KeyboardInterrupt:
            raise
        except:
            if self.debug:
                traceback.print_exc()
            return False
        return True

    def close(self):
        self.s.close()
        self.s = None
    


