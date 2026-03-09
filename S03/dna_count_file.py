#seq_list = ["AGTACACTGGT","ACCAGTGTACT","ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG"]
n = 0
a = 0
c = 0
g = 0
t = 0
#Option 1
f = open("dna.txt", "r")
#Here we put the code
seq_list = f.readlines()
f.close()

#Option 2
with open("dna.txt", "r") as f:
    lines = f.readlines()
# Using this, the close function is automatically called, therefore ensuring the file won't remain open

for seq in seq_list:
    seq = seq.strip() #Remove spaces and newline characters at the end of the string
    n += len(seq)
    for base in seq:
        if base == "A":
            a += 1
        elif base == "C":
            c += 1
        elif base == "G":
            g += 1
        else:
            t += 1
print("There is a total of",n ,"bases, divided into",a, "adenines,",c, "cytosines,",g, "guanines and",t, "thymines")

#To import functions between projects:
# import -function name- from -project name.
#Additionaly, the rest of the original project must be introduced into a new function ==> "main"
#and thhe following must be added:
# if __name__ == "__main__":
# main()





