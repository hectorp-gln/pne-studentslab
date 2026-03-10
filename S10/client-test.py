import socket
from Client0 import Client

IP = "212.128.255.73"
PORT = 8080

c = Client(IP, PORT)

for n in range (0,5):
    message = "Message " + str(n)
    print(f"To Server {message}")
    response = c.talk(message)
    print(f"From Server¨: {response}")