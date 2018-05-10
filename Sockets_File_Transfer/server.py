#File Transfer Server using Socket
#--> https://bit.ly/2KSMT0o 

import os
import sys
import socket

host = 'localhost'; port = 5555
Server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Server.bind((host, port))
Server.listen(5)

print("Initialized server at %s : %s" % (host, port))
filefound = False

while True:
  connection, address = Server.accept()
  print("Connected to client at:", address)
  
  filename = connection.recv(1024).decode('utf-8')
  for f in os.listdir('server_files/'):
    if f == filename: filefound = True

  if filefound:
    print(filename, 'file found on server')
    uploadFile = open('server_files/'+filename, 'rb')
    file_bytes = uploadFile.read(1024)

    while file_bytes:
      connection.send(file_bytes)
      file_bytes = uploadFile.read(1024)
    print("Sent file succesfully")

  else: print('\n',filename, "not found on server\n")
  break

connection.close()
Server.close()
    
