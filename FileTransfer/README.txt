## Transfer files over a network using Python Sockets

#### How to start a Server:
'''
Daemon = Server(host= 'localhost',
                port= 8888 )

Daemon.listen(transfer_protocol='GridFTP')
'''

#### How to connect to server as a *local* client:
client = Client( host='localhost', 
                   port= 8888)


##### A Client can send requests to the Server:
'''
client.request_files(3)
'''
