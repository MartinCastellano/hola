#!python3

import socket ,sys ,time

s = socket.socket()

host = socket.gethostname()

print('server start on host: ',host)

port = 1234 

s.bind((host,port))

print('server conectado ')

s.listen(1)

conn,addr = s.accept()

print(addr,' conectado ')

while 1 :
    msn = input(str('ingrese mensaje '))
    msn = msn.encode()
    conn.send(msn)
    msn_in = conn.recv(1024)
    msn_in = msn_in.decode()
    print('mensaje cliente: ',msn_in)