
import socket

if __name__ == "__main__":
    host = '127.0.0.1'
    port = 5000

    s = socket.socket()
    s.connect((host, port))

    filename = input("Enter a filename: ")
    if filename not in ['quit', 'q', 'exit']:
        s.sendall(filename.encode('utf-8'))
        data = s.recv(1024)
        if data[:6] == 'EXISTS':
            filesize = float(data[6:])
            message = input('File Exists, size is', str(filesize),
                            'Bytes\n Download (y/n)? ')
            if message.lower() == 'y':
                s.send(b'OK')
                f = open('new_'+filename, 'wb')
                data = s.recv(1024)
                totalRecv = len(data)
                f.write(data)
                while totalRecv < filesize:
                    data = s.recv(1024)
                    totalRecv += len(data)
                    f.write(date)
                    print('{0:.2f}% done'.format((totalRecv/filesize*100)))
                print('Download Complete!')

        else:
            print('File does not exist.')

    s.close()
