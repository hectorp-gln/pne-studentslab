import socket

IP = "212.128.255.73"
PORT = 8080

ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #This line makes it so there is no issues with the port
ls.bind((IP,PORT))
ls.listen()
print("The server is running")

while True:
    print("Waiting for a client to connect...")

    try:
        (cs, client_ip_port) = ls.accept()

    except KeyboardInterrupt:
        print("Server stopped by the user")
        ls.close()
        exit()

    else:
        message_raw = cs.recv(2048)
        message = message_raw.decode()
        print("A client has successfully connected!")
        print(f"Received message: {message}")

        response = "Hiiii! I'm the happy server :-) \n"
        cs.send(response.encode())

        ls.close()