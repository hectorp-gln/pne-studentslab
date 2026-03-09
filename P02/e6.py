from Client0 import Client
from Seq1 import Seq

print(f"-----| Practice 2, Exercise 4 |------")

IP = "172.17.255.255"
PORT1 = 8080
PORT2 = 8081

c1 = Client(IP, PORT2)
c2 = Client(IP, PORT2)

print(c1)
print(c2)

s = Seq()
s.read_fasta("sequences/FRAT1.txt")
i = 0
while i < 5:
    message1 = "Fragment " + str(i + 1)+ ": " + str(s)[i * 10:(i + 1) * 10]
    message2 = "Fragment " + str(i + 2) + ": " + str(s)[(i+1) * 10:(i + 2) * 10]
    print(message1)
    print(message2)
    c1.talk(message1)
    c2.talk(message2)
    i += 2