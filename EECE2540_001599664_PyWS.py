#Matthew Egg
#NUID: 001599664

# Import socket package
from socket import *

# Initialize socket location and port number
address = 'localhost'
port_number = 12005
identifier = (address, port_number)

# Create and bind server location
server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(identifier)
print("Server socket created and bound at: ", identifier)

# Make the server accept up to five connections
server_socket.listen(5)
print("Server socket is now listening for connections.")

state = True

while state:
    connection_socket, client_address = server_socket.accept()
    print("Server created connection socket for client at:", client_address)

    message_from_client = connection_socket.recv(2048)
    print("Server received message from client at:", client_address)

    client_string = message_from_client.decode()
    print( "Received string:" , client_string)

    nums = client_string.split('-')
    ints = [int(x) for x in nums]
    sum = str(sum(ints))
    sentStr = "RESULT:" + sum
    message_to_client = sentStr.encode()
    connection_socket.send(message_to_client)
    state = False

server_socket.close()
print("Server socket closed.")
print("Server program terminated.")