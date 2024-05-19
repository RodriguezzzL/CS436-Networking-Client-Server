import socket
import threading


def handle_client(client_socket):
    # Receive data from the client
    request_data = client_socket.recv(4096)
    print("[*] Received request from client:", request_data)