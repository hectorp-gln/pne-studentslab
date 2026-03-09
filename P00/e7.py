from Seq0 import seq_complement, seq_read_fasta

file = "sequences/U5.txt"

if __name__ == "__main__":
    frag = seq_read_fasta(file)[:20]
    comp = seq_complement(frag)
    print("-"*7 ,"|Exercise 7|", "-"*7, "\n", "Gene", file,"\n", "Frag:", frag, "\n", "Comp:", comp  )