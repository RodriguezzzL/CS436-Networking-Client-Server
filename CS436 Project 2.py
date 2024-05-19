import socket
import threading

def handle_client(client_socket):
    
    request_data = client_socket.recv(4096)
    print("[*] Received request from client:", request_data)

    
    remote_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    remote_socket.connect(("www.example.com", 80))
    remote_socket.sendall(request_data)

    
    remote_response = remote_socket.recv(4096)
    print("[*] Received response from server:", remote_response)

   
    client_socket.sendall(remote_response)

    
    remote_socket.close()
    client_socket.close()

def start_proxy():
    
    proxy_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    
    proxy_socket.bind(("127.0.0.1", 8080))

    
    proxy_socket.listen(5)
    print("[*] Proxy listening on port 8080...")

    while True:
        
        client_socket, client_addr = proxy_socket.accept()
        print("[*] Accepted connection from:", client_addr)

       
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    start_proxy()
