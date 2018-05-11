# Python Advanced Tutorial 6.6 Simple File Server
# https://youtu.be/LJTaPaFGmM4

import os
import socket
import threading

def getFile(name, sock):
    filename = sock.recv(1024)
    if os.path.isfile(filename):
        sock.send("EXISTS " + str(os.path.getsize(filename)))
        userResp = sock.recv(1024)
        if userResp[:2] == 'OK':
            with open(filename, 'rb') as f:
                bytesToSend = f.read(1024)
                sock.send(bytesToSend)
    else:
        sock.send('ERROR:\"%s\" does not exist' %s (filename) )
    sock.close()

if __name__ == '__main__':
    host = '127.0.0.1'
    port = 5000

    s = socket.socket()
    s.bind((host, port))
    s.listen(5)

    print('Server Started')

    while True:
        c, addr = s.accept()
        print('Client connected to ip: ' + str(addr))
        t = threading.Thread(target=getFile, args=('retrThread', c))
        t.start()

    s.close()
    
