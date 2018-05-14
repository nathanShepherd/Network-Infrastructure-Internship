# Configure client to download files from a server
# Developed by Nathan Shepherd

import socket
import time

class Client:
  def __init__(self, host='localhost', port= 8888):
    self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('\nConnected to server at', host, port)
    self.socket.connect((host,port))
    self.address = (host, port)

  def request_files(self, num_files):
    ''' REQUEST num_files from Server '''

    print('Sent GET request to server for %s files'%str(num_files))
    self.socket.send(str.encode('GET FILES '+ str(num_files)))
    resp = self.socket.recv(1024).decode().split(' ')
    print('Server response:', resp)
    
    if resp[0] == 'GOOD' and resp[2] == 'GridFTP':
      print('Starting download of %s files via %s'% (resp[1], resp[2]))
      num_files = resp[1]  # upper bounded by num files on server

      # receive pivotal endpoints addresses and connect

      for f in range(int(num_files)):
        confirmation_to_server = b'OK'
        self.socket.send(confirmation_to_server)
        file_info = self.socket.recv(1024).decode()
        fileSize = int(file_info.split(' ')[-1])
        filename = file_info.split(' ')[0].split('/')[-1]

        start = time.time()
        # receive file bytes as dict ordinality:bytes
        # compile file locally

        # Initialize file to be compiled locally
        with open('new_' + filename, 'wb') as f:
          print("\nCompiling file locally: new_" + filename)

          # Receive first batch of file information
          data = self.socket.recv(1024)
          total_recv = len(data)
          print('[', end='')
          f.write(data)
          # print("Received", data, "from Server")

          # Iteratively build the file until no data received
          while data and total_recv < fileSize:
            if int(total_recv * 100 / fileSize) % 50 == 0:
              print('==', end='')
            data = self.socket.recv(1024)
            total_recv += len(data)
            f.write(data)
          print(']')

          download_speed = round((time.time() - start) * 1000, 3)
          print('DownTime', download_speed, 'milliseconds')
          print('Received', total_recv, 'bytes')
          print('Download Complete!')

    elif resp[0] == 'GOOD' and resp[2] == 'FTP':
      print('Starting download of %s files via  %s '% (resp[1], resp[2]))
      num_files = resp[1]# upper bounded by num files on server

      for f in range(int(num_files)):
        confirmation_to_server = b'OK'
        self.socket.send(confirmation_to_server)
        file_info = self.socket.recv(1024).decode()
        fileSize = int(file_info.split(' ')[-1])
        filename = file_info.split(' ')[0].split('/')[-1]

        start = time.time()

        # Initialize file to be compiled locally
        with open('new_' + filename, 'wb') as f:
          print("\nCompiling file locally: new_" + filename)

          # Receive first batch of file information
          data = self.socket.recv(1024)
          total_recv = len(data)
          print('[', end='')
          f.write(data)
          #print("Received", data, "from Server")

          # Iteratively build the file until no data received
          while data and total_recv < fileSize:
            if int(total_recv*100/fileSize) % 50 == 0:
              print('==', end='')
            data = self.socket.recv(1024)
            total_recv += len(data)
            f.write(data)
          print(']')
          
          download_speed = round((time.time() - start)*1000, 3)
          print('DownTime', download_speed, 'milliseconds')
          print('Received', total_recv, 'bytes')
          print('Download Complete!')

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
  client = Client( host='172.16.3.233', 
                   port= 8888)
  client.request_files(8)
  #client.send_msg("Hello!")
