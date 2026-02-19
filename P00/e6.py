from Seq0 import reverse, seq_read_fasta

file = "sequences/U5.txt"

if __name__ == "__main__":
    fragment, reverse = reverse(seq_read_fasta(file),20)
    print("-"*7 ,"|Exercise 6|", "-"*7, "\n", "Gene", file,"\n", "Fragment:", fragment, "\n", "Reverse:", reverse  )
