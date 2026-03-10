from Client0 import Client
from Seq1 import Seq

print(f"-----| Practice 2, Exercise 5 |------")

IP = "212.128.254.240"
PORT = 8080

c = Client(IP, PORT)

print(c)
s = Seq()
s.read_fasta("sequences/FRAT1.txt")
c.talk("Sending the FRAT1 Gene to the server...")
i = 0
while i < 5:
    message = "Fragment " + str(i+1)+ ": " + str(s)[i * 10:(i + 1) * 10]
    print(message)
    c.talk(message)
    i +=1
