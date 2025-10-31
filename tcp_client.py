import socket
import sys

repeat = True
while repeat:
    while True:
        try:
            server = input('Enter server address: ')
            port = int(input('Enter port: '))

            message = str(input('Enter your message: '))
            message = message.encode('utf-8')
            # create tcp socket
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server_address = (server, port)
            print('Connecting to ' + str(server_address))
            sock.connect(server_address) # connect to server using given info.
            break
        except TimeoutError:
            print('Timeout error\n')
        except Exception as e:
            print('Error try again\n')
    
    try:
        print('sending message: ' + str(message))    
        sock.sendall(message) # send the entire message to the server
        amount_received = 0
        amount_expected = len(message) # because we expect to receive the same message but in caps
        while amount_received < amount_expected:
            data = sock.recv(2048)
            amount_received += len(data)
            print('Received ' + str(data))
    finally:
        repeat = input('Send another message? Y/N: ')
        repeat = True if repeat == 'Y' else False # keep program looping if user chooses to
    print('Closing socket\n\n\n')
    sock.close()