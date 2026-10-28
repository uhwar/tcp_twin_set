import socket

HOST = "127.0.0.1"
PORT = 5000

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((HOST, PORT))
        print(f"Connected to {HOST}:{PORT}")

        while True:
            message = input("> ")

            if message == "quit":
                print("Closing client")
                break

            client.sendall(message.encode("utf-8"))
            data = client.recv(1024)

            if not data:
                print("[ERROR] Server closed the connection")
                break

            print(f"Echo: {data.decode('utf-8')}")

except ConnectionRefusedError:
    print(f"[ERROR] Could not connect to {HOST}:{PORT}. Is the server running?")
except ConnectionResetError:
    print("[ERROR] The server reset the connection")
except BrokenPipeError:
    print("[ERROR] The connection was closed while sending data")
except KeyboardInterrupt:
    print("\nClient stopped by user")
except OSError as error:
    print(f"[SOCKET ERROR] {error}")
