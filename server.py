import socket

HOST = "127.0.0.1"
PORT = 5000

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((HOST, PORT))
        server.listen()

        print(f"Listening on {HOST}:{PORT}")

        while True:
            conn, addr = server.accept()
            print(f"Connected by {addr}")

            try:
                with conn:
                    while True:
                        data = conn.recv(1024)

                        if not data:
                            break
                        text = data.decode()
                        reply = text[::-1]

                        conn.sendall(reply.encode())

                print(f"Closed {addr}")

            except ConnectionResetError:
                print(f"[ERROR] The client {addr} reset the connection")
            except OSError as error:
                print(f"[SOCKET ERROR] Client {addr}: {error}")

except KeyboardInterrupt:
    print("\nServer stopped by user")
except OSError as error:
    print(f"[SERVER ERROR] {error}")
