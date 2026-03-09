from Seq0 import seq_count_base, seq_read_fasta

gene_list = ["U5","ADA","FRAT1","FXN"]
bases = ["A","C","T","G"]

if __name__ == "__main__":
    print("-"*5,"|Exercise 4|","-"*5)
    for gene in gene_list:
        print("Gene", gene)
        for base_type in bases:
              print( base_type, ":", seq_count_base(seq_read_fasta("sequences/" + gene + ".txt"),base_type))