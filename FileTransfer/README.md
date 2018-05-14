## Transfer files over a network using Python Sockets

### How to start a Server:
```
from server import Server
from client import Client
```
```
Daemon = Server( host= 'localhost',
                 port= 8888 )
```
#### Configure the Server communication method:
```
Daemon.listen( transfer_protocol = 'GridFTP' )
```

### How to connect to Server as a *local* Client:
```
client = Client( host= 'localhost', 
                 port= 8888)
```

#### A Client can send requests to the Server:
```
client.request_files(1)
```

Executing the above command results in the following log printing to the client-side terminal:
```
Connected to server at 127.0.0.1 8888
Sent GET request to server for 1 files
Server response: ['GOOD', '1', 'GridFTP']
Starting download of 1 files via GridFTP

Compiling file locally: new_html.txt
[========================================]
DownTime 41.519 milliseconds
Received 1063074 bytes
Download Complete!
```













