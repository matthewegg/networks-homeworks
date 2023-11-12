# Matthew Egg, NUID: 001599664
# My client design works by distinguishing a server IP address and range of valid port numbers to connect with, and if successful, send the provided introduction message, awaits a response, and if not failed, then begins solving the expressions sent by the server until the server is satisfied, after which the expression solver loop is exited and the server's response is printed, whether an expression response was incorrect or the client was successful.
# My code was tested by using the sample server to see if the expected contact could be correctly achiveve, with different print statements to mark the succesful entry of different aspects of the code. I ran into the usual syntax errors and small logic blunders, such as making the while loop condition if the server message WAS "SUCC" or "FAIL" which is the inverse of what was to be expected, or forgetting to encode a message before sending to the server. Another issue that I encountered was that on occasion, it appears that the server doesn't send back a message at random in the process, which resulted in my client program being timed out after long enough. I assumed that my program was doing something wrong until I included an iteration message every time a message was completed as a means of being sure that my loop was being entered, and that the client was solving the expressions.
# My flag: 30ae7861143dbf1d57aa1464653b5470fe35a338973693efd67b5615e1e87548

from socket import *

server_address = '129.10.131.26'    # Given server IP address
server_port_range = (12000, 12011)  # Given server port range
buffer_size = 4096                # Given buffer size
#server_identifier = (server_address, server_port_range)

for port in server_port_range:    # Loop to try each port in the range
    try:
        client_socket = socket(AF_INET, SOCK_STREAM)
        client_socket.settimeout(2)
        client_socket.connect((server_address, port))
        break
    except socket.error:    # If connection attempt fails, try next port
        print(f'Connection attempt to {server_address}:{port} failed')

#client_socket = socket(AF_INET , SOCK_STREAM)
#client_socket.connect(server_identifier)

welcome_message = 'EECE2540 INTR 001599664'   # Given welcome message
client_socket.send(welcome_message.encode())    # Send welcome message
server_message = client_socket.recv(buffer_size).decode('utf-8')    # Receive server response

while (server_message.find('SUCC') == -1 and server_message.find('FAIL') == -1):    # Loop to solve expressions until server is satisfied, or an expression result fails
    if (server_message.find('EXPR') != -1):   # If server message is an expression
        if server_message.find('+') != -1:  # If cases for each operation type
            expression = server_message[14:].split('+')  # Split expression into operands
            result = int(expression[0]) + int(expression[1])    # Solve expression
        elif server_message.find('-') != -1:
            expression = server_message[14:].split('-')
            result = int(expression[0]) - int(expression[1])
        elif server_message.find('*') != -1:
            expression = server_message[14:].split('*')
            result = int(expression[0]) * int(expression[1])
        elif server_message.find('/') != -1:
            expression = server_message[14:].split('/')
            result = int(expression[0]) / int(expression[1])
            
        message = ('EECE2540 RSLT ' + str(result)).encode()   # Create result message with solution
        client_socket.send(message)   # Send result message
    server_message = client_socket.recv(buffer_size).decode('utf-8')    # Receive server response

client_socket.close()   # Close socket
print(server_message)   # Print final server response, either a failure message or a success message with flag