#!python3

import socket ,sys ,time
import  pickle

s = socket.socket()

host = input(str('enter host '))

port = 1234

s.connect((host,port))

while 1 :
    msn_in = s.recv(1024)
    msn_in = msn_in.decode()
    print('mensaje server: ',msn_in)
    msn = input(str('ingrese mensaje '))
    msn = msn.encode()
    s.send(msn)