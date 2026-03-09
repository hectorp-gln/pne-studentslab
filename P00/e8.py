from Seq0 import seq_count, seq_read_fasta

gene_list = ["U5","ADA","FRAT1","FXN"]

if __name__ == "__main__":
    print("-"*8,"|Exercise 8|","-"*8)
    for gene in gene_list:
        highest_freq = 0
        highest_freq_key = ""
        bases_dict = seq_count(seq_read_fasta("sequences/" + gene + ".txt"))
        for key in bases_dict:
            if bases_dict[key] > highest_freq:
                highest_freq = bases_dict[key]
                highest_freq_key = key
        print("Gene", gene, ":", "Most frequent base:", highest_freq_key)
