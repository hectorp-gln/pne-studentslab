import socket
import termcolor
from NumGss import NumberGuesser

IP = "127.0.0.1"
PORT = 8080

listening_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listening_s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #This line makes it so there is no issues with the port
listening_s.bind((IP,PORT))
listening_s.listen()

a = NumberGuesser()
print("Number generated, start making your guess.")

while True:
    try:
        (client_s, client_ip_port) = listening_s.accept()

    except KeyboardInterrupt:
        print("Server stopped by the user")
        listening_s.close()
        exit()

    else:
        message_raw = client_s.recv(2048)
        response = a.guess(message_raw.decode())
        termcolor.cprint(f"Received message: {message_raw.decode()}", "green")


        client_s.send(response.encode())

        client_s.close()