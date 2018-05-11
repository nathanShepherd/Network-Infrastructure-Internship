#File Transfer Server using Socket
#--> https://bit.ly/2KSMT0o 

import os
import sys
import socket

host = '0.0.0.0'; port = 60600
Server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Server.bind((host, port))
Server.listen(5)

print("Initialized server at %s : %s\n" % (host, port))
filefound = False

while True:
  connection, address = Server.accept()
  print("Connected to client at:", address, end='\n\n')
  
  filename = connection.recv(1024).decode('utf-8')
  for f in os.listdir('files/'):
    if f == filename: filefound = True

  if filefound:
    print(filename, 'file found on server\n')
    uploadFile = open('files/'+filename, 'rb')
    file_bytes = uploadFile.read(1024)

    while file_bytes:
      connection.send(file_bytes)
      file_bytes = uploadFile.read(1024)
    print("Sent file succesfully")

  else: 
    print('\n',filename, "not found on server\n")
    raise NameError

  break

connection.close()
Server.close()
    
