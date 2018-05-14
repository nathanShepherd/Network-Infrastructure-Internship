## Transfer files over a network using Python Sockets

### How to start a Server:
```
Daemon = Server( host= 'localhost',
                 port= 8888 )
```
```
Daemon.listen(transfer_protocol='GridFTP')
```

### How to connect to Server as a *local* Client:
```
client = Client( host= 'localhost', 
                 port= 8888)
```

#### A Client can send requests to the Server:
```
client.request_files(3)
```

##### Incanting above command results in the following log printing to terminal:
```
Compiling file locally: new_html_(4th_copy).txt
[========================================]
DownTime 41.519 milliseconds
Received 1063074 bytes
Download Complete!
```













