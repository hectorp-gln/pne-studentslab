from Seq1 import Seq

list_files = ["U5","ADA","FRAT1","FXN","RNU6_269P"]
for filename in list_files:
    s = Seq()
    s.read_fasta("sequences/"+filename+".txt")
    highest_freq = 0
    highest_freq_key = ""
    for key in s.count():
        if s.count()[key] > highest_freq:
            highest_freq = s.count()[key]
            highest_freq_key = key
    print("Gene", filename, ":", "Most frequent base:", highest_freq_key)
