import socket
import json

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 1234

server_socket.bind((host, port))
server_socket.listen(1)

with open("dictionary.json", "r") as file:
    int_str_dictionary = json.load(file)

while True:
    client_socket, client_addr = server_socket.accept()
    key = client_socket.recv(1024).decode()
    try:
        print(f"Received key: {key}")
    except ValueError:
        print("Invalid input. Please send an integer.")
        client_socket.send("Invalid".encode())
        client_socket.close()
        continue

    client_socket.send((int_str_dictionary.get(key, "Invalid")).encode())
    client_socket.close()
server_socket.close()
