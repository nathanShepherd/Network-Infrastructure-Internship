# Setup a Server that can communicate with a client
# Communication is executed via an asynchronous network channel
# Started from StackOverflow @ https://bit.ly/2KinUCC

'''%%%%%%%%% GridFTP Protocol %%%%%%%%%%'''
# 1. UploadFile is compressed and digitized
# 2. Multiple TCP conduits send UploadFile simultaniously
# 3. UploadFile is compiled on the client side

# Developed by Nathan Shepherd


import threading
import socket
import glob
import os

class Endpoint():
  def __init__(self, connection, address):
    self.connection = connection
    self.address = address
  
  def start_thread(self, target, args=None):
    self.thread = threading.Thread(target=target)
    self.thread.start()

  def config(self, method='TCP'):
    # Use typing to determine which endpoint to configure

    if method == 'TCP':# Using FTP Protocol
      self.start_thread(self.fileTransfer())

    if method == 'GridFTP':# Using distributed TCP implimentation
      self.start_thread(self.asynchronousFileTransfer())

    if method == 'Pivot':
      self.start_thread(self.pivot())
  
  def pivot(self):
    # 1. Configure endpoints and connect each to Server    
    # 2. Each endpoint starts listening for connections
    client_host, client_port = self.address
    client_connection = self.connection

    # Copy the protocol for self.fileTransfer
    # Adapt pivot to send enumerated bytes to client

  def asynchronousFileTransfer(self):
    # Authentication protocol with client
    clnt_auth = self.connection.recv(1024).decode().split(' ')
    if clnt_auth == '': print('Client authentication error')
    print("Client status:", clnt_auth)

    max_files = len(glob.glob('./files/*.txt'))
    num_files = int(clnt_auth[-1])

    num_files = min(num_files, max_files)
    self.connection.send(str.encode('GOOD '+str(num_files)+' GridFTP'))

    if 'FILES' in clnt_auth:
      file_ptr, num_sent = 0, 0
      files = glob.glob('files/*.txt')

      while file_ptr <= max_files and num_sent < num_files:
        print('Client status:', self.connection.recv(1024).decode())
        filename = files[file_ptr]
        fileSize = str(os.path.getsize(filename))

        if filename.endswith('.txt'):
          print('\nSending', filename, fileSize, 'to client')
          # Send filename, fileSize to client
          self.connection.send(str.encode(filename+' '+fileSize))
          # print('Sent filename to client')
          
          ############################################
          # %%% Asynchronous File Transfer Protocol %%%
          # 0. Setup a Client and Server connected via Sockets
          # 1. Configure endpoints and connect each to Server
          # 2. Each endpoint starts listening for connections
          # 3. Server sends IPs and Ports of endpoints to Client
          # 4. Client connects to all endpoints
          # 5. Server distributes the file into buckets
          # 6. Each bucket of the file is enumerated
          # 7. File buckets are sent in parralel to Client via endpoints
          # 8. Client reconfigures File locally with respect to enumeration

          # Configure Pivot endpoints
          # Try using UDP protocol to speed up file transfer rate
          # TCP vs. UDP @ https://bit.ly/2IBROnW

          # Enumerate file bytes into a list
          # Send dict of ordinality:bytes to client via Pivots in parallel

          # Begin File Upload
          steps = 0; bytesSent = 0
          with open(filename, 'rb') as f:
            bytesToSend = f.read(1024)
            bytesSent += len(bytesToSend)
            self.connection.send(bytesToSend)
            steps += 1

            # print('sent', bytesToSend, 'to client')
            while bytesToSend:
              steps += 1
              bytesToSend = f.read(1024)
              bytesSent += len(bytesToSend)
              self.connection.send(bytesToSend)

          print(steps, 'steps to send', bytesSent, 'bytes')

          num_sent += 1
          print('Sent %s of %s files to client\n' % (num_sent, num_files))
        # self.connection.close()

        file_ptr += 1
      print('Completed File Upload to client')
      print('===============================\n')
  
  '''   Client decides num_files to download from server     '''
  '''Server uploads min(available_files, num_files) to client'''
  def fileTransfer(self):# Using FTP protocol
    # Authentication protocol with client
    clnt_auth = self.connection.recv(1024).decode().split(' ')
    if clnt_auth=='': print('Client authentication error')
    print("Client status:", clnt_auth)

    max_files = len(glob.glob('./files/*.txt')) 
    num_files = int(clnt_auth[-1])

    num_files = min(num_files, max_files)
    self.connection.send(str.encode('GOOD '+ str(num_files) + 'FTP'))

    if 'FILES' in clnt_auth:
      file_ptr, num_sent = 0, 0
      files = glob.glob('files/*.txt')
      
      while file_ptr <= max_files and num_sent < num_files:
          print('Client status:', self.connection.recv(1024).decode())
          filename = files[file_ptr]
          fileSize = str(os.path.getsize(filename))

          if filename.endswith('.txt'):

            print('\nSending', filename, fileSize,'to client')
            
            # Send filename to client
            self.connection.send(str.encode(filename +' '+fileSize))
            #print('Sent filename to client')

            # Begin File Upload
            with open(filename, 'rb') as f:
              bytesToSend = f.read(1024)
              self.connection.send(bytesToSend)
              #print('sent', bytesToSend, 'to client')
              while bytesToSend:
                #print('In Loop')
                bytesToSend = f.read(1024)
                self.connection.send(bytesToSend)

            num_sent += 1
            print('Sent %s of %s files to client\n'% (num_sent, num_files))
          #self.connection.close()

          file_ptr += 1
      print('Completed File Upload to client')
      print('===============================')
    

  def sendString(self, addr):
    print("Sending bytes to Client:", addr)
    msg ='You are connected to a server at '
    msg += str(addr[0]) + ' ' + str(addr[1])

    self.connection.send(str.encode(msg))

class Server:
  def __init__(self, host='localhost', port=6438):
    self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print ('\nInitializing server at:', host, port)
    self.serverSocket.bind((host, port))

    self.clientele = []

  def listen(self, max_clients=5, transfer_protocol='TCP'):
    self.serverSocket.listen(max_clients)                                        
    print('Server started and ready to communicate with client(s)')
    print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n')

    while True:
      clientSocket, addr = self.serverSocket.accept()
      print("Client connected at",  (addr))
      print("Using transfer protocol \'%s\']"% transfer_protocol)
      clnt = Endpoint(clientSocket, addr)
      clnt.config(transfer_protocol)
      self.clientele.append(clnt)

if __name__ == "__main__":
  Daemon = Server(host= '172.16.3.233',
                  port= 8888 )
  Daemon.listen(transfer_protocol='GridFTP')





