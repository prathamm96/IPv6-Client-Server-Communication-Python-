import socket

def ipv6_client(host="::1", port=1043):
    try:
        # Create IPv6 TCP socket
        client_socket = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
        client_socket.connect((host, port))
        print(f"[CLIENT] Connected to server [{host}]:{port}")

        # Receive welcome message
        msg = client_socket.recv(1024).decode().strip()
        print(f"[CLIENT] Server says: {msg}")

        # Send message to server
        client_socket.send(b"Hello Server, this is IPv6 Client!\n")

        # Get server response
        reply = client_socket.recv(1024).decode().strip()
        print(f"[CLIENT] Server replied: {reply}")

        client_socket.close()
        print("[CLIENT] Connection closed.")

    except ConnectionRefusedError:
        print(f"[ERROR] Could not connect to [{host}]:{port}. Is the server running?")
    except Exception as e:
        print(f"[ERROR] {e}")

if __name__ == "__main__":
    ipv6_client()
