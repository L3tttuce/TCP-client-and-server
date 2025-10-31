import socket
import sys

server = '' 
port = int(input('Which port do you want to listen on? '))
# create tcp socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = (server, port)
print('Running on ' + server + ' using port ' + str(port))
# associate server with ip (current server, port number)
sock.bind(server_address)
sock.listen(5)

while True:
    print('Waiting for connection')
    connection, client_address = sock.accept() # accept incoming connection
    try:
        print('Connected to, ' + str(client_address))
        while True:
            data = connection.recv(2048) # store data that is received
            print('received: ' + str(data))
            if data:
                message = data.decode('utf-8')
                print(str(message))
                message = message.upper() # capitalize every letter
                print(str(message))
                print('sending data to client')
                connection.sendall(message.encode('utf-8'))
            else:
                print('no more data from, ' + str(client_address))
                break
    finally:
        connection.close()