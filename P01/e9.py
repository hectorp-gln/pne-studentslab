from Seq1 import Seq

s = Seq()
s.read_fasta("sequences/U5.txt")

print(f"Sequence: (Length:", s.len(),")", s, "\n", "Bases:", s.count(),"\n",
      "Rev:", s.reverse(),"\n", "Comp", s.complement())