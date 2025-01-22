import socket
import json

host = '127.0.0.1'
port = 1234

with open("dictionary.json", "r") as file:
    message = json.load(file)

for i in message:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    client_socket.send(str(i).encode())
    response = client_socket.recv(1024).decode()
    print(f"Server response: {response}")

client_socket.close()
