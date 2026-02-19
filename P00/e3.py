from Seq0 import seq_len, seq_read_fasta

gene_list = ["U5","ADA","FRAT1","FXN"]

if __name__ == "__main__":
    print("-"*5,"|Exercise 3|","-"*5)
    for gene in gene_list:
        print("Gene", gene, "-> Length:",seq_len(seq_read_fasta("sequences/" + gene + ".txt")))