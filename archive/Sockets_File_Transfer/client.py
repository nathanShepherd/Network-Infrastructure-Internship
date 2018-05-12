#File Transder Client using Sockets
#--> https://bit.ly/2KSMT0o 

import sys
import time
import socket


#host = 'localhost'; port = 5555
host = '0.0.0.0'; port = 60600
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

filename = input('Enter filename to download from server: ')

while True:
  client.send(str.encode(filename))# send filename to server
  download_file = open('new_'+filename, 'wb')

  start = time.time()
  data = client.recv(1024)# recieve part of file from server
  while data:
    download_file.write(data)# write data into file
    data = client.recv(1024)# receive part of file from server
  print("\nReceived file, download duration:", round(time.time() - start, 6))

  print("\nClosing client connection")

  break

client.close()


