from Client0 import Client

print(f"-----| Practice 2, Exercise 3 |------")

IP = "172.17.255.255"
PORT = 8080

c = Client(IP, PORT)

print(c)
print("Sending a message to the server...")
response = c.talk("Hello server!!!")
print(f"Response:", response)