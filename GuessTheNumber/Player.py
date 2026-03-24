from Client0 import Client

IP = "127.0.0.1"
PORT = 8080

c = Client(IP, PORT)

guess = False
while guess == False:
    message = input("Please enter your guess: ")
    response = c.talk(message)
    print(f"Server says: {response}")
    if response.startswith("You"):
        guess = True