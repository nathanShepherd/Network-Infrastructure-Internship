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


class Endpoint():
  def __init__(self, connection, address, args=None):
    self.connection = connection
    self.address = address

    # Use typing to determine the type of endpoint
    # Add support for FTP FileTransfer
    # Add supoort for asynchronous file transfer
    
    self.thread = threading.Thread(target = self.sendBytes,
                                   args = ("TCP", address))
    self.thread.start()

  def sendBytes(self, protocol, address):
    host, port = address
    print("Sending bytes to Client:", address)
    msg = 'You are connected to a server at '+str(host)+' '+str(port)
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
      clnt = Endpoint(clientSocket, addr)
      self.clientele.append(clnt)
      
      clnt_auth = clientSocket.recv(1024).decode()
      print("Client says:", clnt_auth)

if __name__ == "__main__":
  Daemon = Server(host= 'localhost',
                  port= 8888 )
  Daemon.listen()





