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

class Endpoint():
  def __init__(self, connection, address):
    self.connection = connection
    self.address = address

  def config(self, method='FTP'):
    # Use typing to determine the type of endpoint
    # Add support for FTP FileTransfer
    # Add supoort for asynchronous file transfer
    if method == 'FTP':
      self.start_thread(self.fileTransfer(3))
    
    if method == 'TCP': 
      self.start_thread(self.sendString(self.address))
  
  def start_thread(self, target, args=None):
    self.thread = threading.Thread(target=target)
    self.thread.start()

  def fileTransfer(self, num_files):
    # Authentication protocol with client
    clnt_auth = self.connection.recv(1024).decode().split(' ')
    self.connection.send(str.encode('GOOD '+ str(num_files)))
    print("Client says:", clnt_auth)

    if 'FILES' in clnt_auth:
      file_ptr, num_sent = 0, 0
      num_files = clnt_auth[-1]
      files = glob.glob('./files/*.txt')
      max_files = len(glob.glob('./files/*.txt'))
      
      
      while num_sent <= max_files or num_sent != num_files:
          filename = files[file_ptr]

          if filename.endswith('.txt'):
            # Send filename to client
            self.connection.send(str.encode(filename))
            
            # Begin File Upload
            with open(filename, 'rb') as f:
              bytesToSend = f.read(1024)
              self.connection.send(bytesToSend)
              while bytesToSend != "":
                bytesToSend = f.read(1024)
                self.connection.send(bytesToSend)

            num_sent += 1
            print('Sent %s of %s files to client'% (num_sent, num_files))

          file_ptr += 1
      print('Completed File Upload to client\n=====================')
    

  def sendString(self, addr):
    print("Sending bytes to Client:", addr)
    msg ='You are connected to a server at '
    msg += str(addr[0]) + ' ' + str(addr[1])

    self.connection.send(str.encode(msg))

class Server:
  def __init__(self, host='localhost', port=6438):
    self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print ('Initializing server at:', host, port)
    self.serverSocket.bind((host, port))

    self.clientele = []

  def listen(self, max_clients=5):
    self.serverSocket.listen(max_clients)                                        
    print ('Server started and ready to communicate with client(s)')

    while True:
      clientSocket, addr = self.serverSocket.accept()
      print("Client connected at",  (addr))
      clnt = Endpoint(clientSocket, addr); clnt.config()
      self.clientele.append(clnt)
      
      clnt_auth = clientSocket.recv(1024).decode().split(' ')
      print("Client says:", clnt_auth)
      if 'FILES' in clnt_auth:
        num_files = clnt_auth[-1]
        
        
         
      

if __name__ == "__main__":
  Daemon = Server(host= 'localhost',
                  port= 8888 )
  Daemon.listen()





