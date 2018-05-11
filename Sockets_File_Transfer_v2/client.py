
import socket

if __name__ == "__main__":
    host = '127.0.0.1'
    port = 5000
    
    # Connect to server
    s = socket.socket()
    s.connect((host, port))

    filename = input("Enter a filename: ")
    if filename not in ['quit', 'q', 'exit']:

        s.sendall(filename.encode('utf-8'))

        data = s.recv(1024)
        if data[:5] != 'ERROR':

            filesize = float((data.split(b" ")[-1]))
            message = input('File Exists, size is ' + str(filesize) +\
                            ' Bytes\n Download? (y/n): ')

            if message.lower() == 'y':
		# Communicate to server that file exists
                s.send(b'OK')
		
		# initialize the new file to build locally
                f = open('new_'+filename.split('/')[-1], 'wb')

		# Receive the first batch of file information
                data = s.recv(1024)
                totalBytesReceived = len(data)
                f.write(data)

		# Iteratively build the file until 
                #while totalBytesReceived < filesize:
                while data:
                    print(totalBytesReceived, '|', filesize, '% done')
                    #print('Downloading file ...')
                    data = s.recv(1024)
                    totalBytesReceived += len(data)
                    f.write(data)

                print('Download Complete!')

        else:
            print('File does not exist.')

    s.close()

#?
