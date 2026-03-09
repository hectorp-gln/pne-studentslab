seq = input("Introduce the DNA sequence")

len_seq = len(seq)
print("Total lenght:", len_seq, "bases")

a = 0
c = 0
g = 0
t = 0

for base in seq:
    if base == "A":
        a += 1
    elif base == "C":
        c += 1
    elif base == "G":
        g += 1
    else:
        t += 1


print("A:",a, "\n"
    "C:",c, "\n"
    "G:",g, "\n"
    "T:",t, )
