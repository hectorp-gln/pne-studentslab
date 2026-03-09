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

def generate_seq(pattern,n):
    current_seq = ""
    list_seq = []
    i = 1
    while i <= n:
        current_seq += pattern
        list_seq.append(Seq(current_seq))
        i += 1
    return list_seq

seq_list1 = generate_seq("A",3)
seq_list2 = generate_seq("AC",5)

print("List 1:")
print_seqs(seq_list1)

print()
print("List 2:")
print_seqs(seq_list2)
