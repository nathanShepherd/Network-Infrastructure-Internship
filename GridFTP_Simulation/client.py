#! /usr/bin/python3

import socket


class Client:
  def __init__(self, host='localhost', port= 8888):
    self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.socket.connect((host,port))
    self.address = (host, port)

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
  client.send_msg("Hello!")
