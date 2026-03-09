from Seq1 import Seq

def print_seqs(seq):
        print("Sequence 1: (Length: " + str(seq.len()) + ") " + str(seq))

sequence = Seq("ACTGA")
print_seqs(sequence)