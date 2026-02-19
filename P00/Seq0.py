from pathlib import Path

def seq_ping():
    print("OK")

def seq_read_fasta(filename):
    file_contents = Path(filename).read_text()
    non_header = file_contents.split("\n")[1:-1]
    sequence = "".join(non_header)
    return sequence

def seq_len(seq):
    return len(seq)

def seq_count_base(sequence, chosen_base):
    count = 0
    for base in sequence:
        if base == chosen_base:
            count += 1
    return count

def seq_count(sequence):
    bases = {"A": 0,"C": 0, "G": 0,"T": 0}
    for base_type in bases.keys():
        bases[base_type] = seq_count_base(sequence, base_type)
    return bases

def reverse(sequence, n):
    fragment = sequence[:n]
    reverse = fragment [::-1]
    return fragment, reverse

def seq_complement(sequence):
    compliment_dict = {"A":"T","T":"A","C":"G","G":"C"}
    new_seq = ""
    for base in sequence:
        new_seq += compliment_dict[base]
    return new_seq


