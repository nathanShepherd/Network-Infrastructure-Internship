#Python 3 Programming Tutorial - Sockets: client server system
#--> youtube.com/watch?v=Q1a12QFq3os 

import sys
import socket
from _thread import *

host = ''
port = 5555
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
  s.bind((host, port))
except socket.error as e:
  print(str(e))

s.listen(5)
print("Initialized server at port:", port)

def threaded_client(connection):
  connection.send(str.encode('Input your info:\n'))
  
  while True:
    data = connection.recv(2048)
    reply = 'Server output: ' + data.decode('utf-8')
    if not data or data.decode('utf-8') == 'q': break

    connection.sendall(str.encode(reply))
  connection.close()



while True:
  conn, addr = s.accept()
  #Connect using: [./local]$ telnet localhost <port>
  print('connected to:', addr[0]+':'+str(addr[1]))
  
  start_new_thread(threaded_client, (conn,))
