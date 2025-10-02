import socket

def ipv6_server(host="::1", port=1043):
    try:
        
        server_socket = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
        server_socket.bind((host, port))
        server_socket.listen(1)
        print(f"[SERVER] IPv6 Server listening on [{host}]:{port} ...")

        conn, addr = server_socket.accept()
        print(f"[SERVER] Connection from {addr}")

      
        conn.send(b"Hello from (Pratham Jariwala) IPv6 server!\n")

        
        data = conn.recv(1024).decode().strip()
        print(f"[SERVER] Client says: {data}")

   
        conn.send(b"Message received. Goodbye! Yamya Sir !!\n")

        conn.close()
        server_socket.close()
        print("[SERVER] Connection closed.")

    except PermissionError:
        print(f"[ERROR] Permission denied for port {port}. Try running as Administrator or use a port >1023.")
    except Exception as e:
        print(f"[ERROR] {e}")

if __name__ == "__main__":
    ipv6_server()
