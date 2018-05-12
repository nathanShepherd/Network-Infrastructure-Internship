# Standard testing for various File Transfer Protocol
# Developed by Nathan Shepherd

#import threading
#from server import Server
from client import Client

if __name__ == "__main__":
  client = Client()
  client.send_msg("Hello!") 
