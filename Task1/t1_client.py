import socket

# client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '127.0.0.1'
port = 1234

# client_socket.connect((host, port))

message = [1, 2, 3]

for i in message:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    client_socket.send(str(i).encode())
    response = client_socket.recv(1024).decode()
    print(f"Server response: {response}")

client_socket.close()