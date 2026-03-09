class Seq:
    def __init__(self, strbases):
        self.bases = strbases
        print("New sequence created!")

    def __str__(self):
        return self.bases

    def len(self):
        return len(self.bases)

def print_seqs(sequen_list):
    for seq in sequen_list:
        print("Sequence " + str(sequen_list.index(seq)) + ": (Length: " + str(seq.len()) + ") " + str(seq))

seq_list = [Seq("ACT"), Seq("GATA"), Seq("CAGATA")]

print_seqs(seq_list)



