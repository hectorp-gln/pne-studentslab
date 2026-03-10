import socket
import termcolor

IP = "212.128.255.73"
PORT = 8080
connections = 0
client_info = []

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
        if connections < 5:
            print("A client has successfully connected!")
            connections += 1

            client = "Client " + str(connections) + ": " + str(client_ip_port)
            client_info.append(client)

            message_raw = client_s.recv(2048)
            message = termcolor.colored(message_raw.decode(), "green")
            print(f"Received message: {message}")

            response = "ECHO: " + message + "\n"
            client_s.send(response.encode())

            client_s.close()

        else:
            print("The following clients have connected to the server:", "\n")
            for info in client_info:
                print(info)
            listening_s.close()
            exit()