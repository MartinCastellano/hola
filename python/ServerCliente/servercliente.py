#! python3

import socket
import threading
import sys
import time
from random import randint

SERVER = socket.gethostbyname(socket.gethostname())#gethostname solo sirve cuando el server y el cliente estan en la misma maquina
#iriea la ip addres
class Server():

    Connections = []
    peers = []
    def __init__(self):

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)         
        sock.bind((SERVER, 1024))
        sock.listen(5)#indica cuantas conexiones pueden estar en cola 
        # sock.setblocking(False)

        print("Server running...")
        
        while True:
            c, a =  sock.accept()
            cThread = threading.Thread(target=self.handler, args=(c, a))
            
            cThread.daemon = True
            cThread.start()
            self.Connections.append(c)
            self.peers.append(a[0])
            print(str(a[0]) + ':' + str(a[1]), "connected")
            # print(f'{a} connected')
            self.sendPeers()


    def handler(self, c, a):
        
        while True:
            data = c.recvfrom(1024)
            for connection in Connections:
                connection.send(data)
            if not data:
                print(str(a[0]) + ':' + str(a[1]), "connected")
                self.Connections.remove(c)
                self.peers.remove(a[0])
                c.close()
                self.sendPeers() 
                break

    def sendPeers(self):
        p=""
        for peer in self.peers:
            p = p + peer + ","

        for connection in self.Connections:
            Connections.send(b'\x11' + bytes(p, "utf-8"))              
class Client():

    def sendMsg(self,sock):
        while True:
            sock.send(bytes(input(""), 'utf-8'))
                
    def __init__(self,address):

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.connect((address, 1024))

        iThread = threading.thread(target=self.sendMsg, args=(sock,))
        iThread.daemon = True
        iThread.start()

        while True:
            data = sock.recvfrom(1024)
            if not data:
                break
            if data[0:1] == b'\x11': 
                self.updatePeers(data[1:])
                                        
            else:
                print(str(data, 'utf-8'))

    def updatePeers(self, peerData):
        p2p.peers = str(peerData, "utf-8").split(",") [:-1]                

class p2p():

    peers = ['127.0.0.1']      

while True:
        
        try:
            print("Trying to connect")
            time.sleep(randint(1, 5))
            for peer in p2p.peers:
                
                try:

                    client = Client(peer)
                except KeyboardInterrupt:
                    sys.exit(0)

                except:
                    
                    pass
                # if randint(1, 20 )==1:
                
                    try:
                        server = Server()
                    except KeyboardInterrupt:
                        sys.exit(0)    
                    except:
                        print("Couldn't start the server..... :( ")    
        except KeyboardInterrupt:
            sys.exit(0)    
        