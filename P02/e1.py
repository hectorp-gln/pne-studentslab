from Client0 import Client

print(f"-----| Practice 2, Exercise 1 |------")

IP = "212.128.255.73"
PORT = 8080

c = Client(IP, PORT)

c.ping()