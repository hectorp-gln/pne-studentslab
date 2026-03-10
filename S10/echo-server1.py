import socket
import termcolor

IP = "212.128.255.73"
PORT = 8080

listening_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listening_s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #This line makes it so there is no issues with the port
listening_s.bind((IP,PORT))
listening_s.listen()
print("The server is running")

while True:
    print("Waiting for a client to connect...")

    try:
        (client_s, client_ip_port) = listening_s.accept()

    except KeyboardInterrupt:
        print("Server stopped by the user")
        listening_s.close()
        exit()

    else:
        message_raw = client_s.recv(2048)
        message = termcolor.colored(message_raw.decode(), "green")
        print("A client has successfully connected!")
        print(f"Received message: {message}")
        response = "ECHO: " + message + "\n"
        client_s.send(response.encode())

        client_s.close()