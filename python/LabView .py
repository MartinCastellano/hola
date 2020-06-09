import struct
import socket 
HOST = '192.168.1.1'
PORT = 6340
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

for x in range(200):
      size = struct.unpack('i', s.recv(4)) [0]
      str_data= s.recv(size)
      print ('Data size: %s Data value: %s' % (size, str_data.decode('ascii')))
s.sendall(b'Enough data :) Thanks')
