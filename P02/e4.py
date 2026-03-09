from Client0 import Client
from Seq1 import Seq

print(f"-----| Practice 2, Exercise 4 |------")

files = ["U5","FRAT1","ADA"]

IP = "172.17.255.255"
PORT = 8080

c = Client(IP, PORT)

print(c)
for filename in files:
    s = Seq()
    s.read_fasta("sequences/" + filename + ".txt")
    c.talk("Sending the" + filename + "Gene to the server...")
    c.talk(s)