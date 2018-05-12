# Configure client to download files from a server
# Developed by Nathan Shepherd

import socket


class Client:
  def __init__(self, host='localhost', port= 8888):
    self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.socket.connect((host,port))
    self.address = (host, port)

  def request_files(self, num_files):
    ''' REQUEST num_files from Server '''

    self.socket.send(str.encode('GET FILES '+ str(num_files)))
    resp = self.socket.recv(1024).decode().split(' ')

    if resp[0] == 'GOOD':
      print('Starting download of %s files'% resp[1])

      for f in range(int(num_files)):
        confirmation_to_server = b'OK'
        self.socket.send(confirmation_to_server)
        file_info = self.socket.recv(1024).decode()
        fileSize = int(file_info.split(' ')[-1])
        filename = file_info.split(' ')[0].split('/')[-1]

        # Initialize file to be compiled locally
        with open('new_' + filename, 'wb') as f:
          print("\nCompiling file locally: new_" + filename +' '+str(fileSize))
        
          # Receive first batch of file information
          data = self.socket.recv(1024)
          total_recv = len(data)
          f.write(data)
          #print("Received", data, "from Server")

          # Iteratively build the file until no data received
          while data and total_recv < fileSize:
            data = self.socket.recv(1024)
            total_recv += len(data)
            f.write(data)
          print('Received', total_recv, 'bytes') 

          print('\nDownload Complete!')

    else: print("\nError authenticating with server")

  def send_msg(self, msg=""):
    while True:
      if msg == "": 
        msg = input("Enter a message: ")
      self.socket.send(msg.encode())

      data = self.socket.recv(1024).decode()
      print("Message from server:", data)

  def __del__(self): self.socket.close()

if __name__ == "__main__":
  client = Client()
  client.request_files(3)
  #client.send_msg("Hello!")
