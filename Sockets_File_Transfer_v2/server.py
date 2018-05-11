# Python Advanced Tutorial 6.6 Simple File Server
# https://youtu.be/LJTaPaFGmM4

import os
import socket
import threading

def getFile(name, sock):
    filename = sock.recv(1024)
    if os.path.isfile(filename):
        sock.send(str.encode("Requested file exists " +\
                              str(os.path.getsize(filename))))

        userResp = sock.recv(1024)
        if userResp[:2] == 'OK':

	    # After client confirmation, send file
            with open(filename, 'rb') as f:
                bytesToSend = f.read(1024)
                sock.send(bytesToSend)

                while bytesToSend != "":
                    bytesToSend = f.read(1024)
                    sock.send(bytesToSend)
    else: 
        # Requested file does not exist
        #sock.sendall('ERROR:\"%s\" does not exist' %s (filename) )
        print('Requested file does not exist')

    sock.close()

if __name__ == '__main__':
    # Server Location
    host = '127.0.0.1'
    port = 5000
    
    # Initialize TCP Connection
    s = socket.socket()
    s.bind((host, port))
    s.listen(5)

    print('Server Started')

    while True:
	#Start new thread iff a new client connects
        c, addr = s.accept()
        print('Client connected via ip: ' + str(addr))
        t = threading.Thread(target=getFile, args=('retrThread', c))
        t.start()

    s.close()
    
#?
