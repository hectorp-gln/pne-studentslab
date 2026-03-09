from Seq0 import seq_read_fasta

if __name__ == "__main__":
    text_file = input("Enter the name of the desired file (including the .txt): ")
    first_20 = seq_read_fasta("sequences/" + text_file)[:20]
    print("DNA file", text_file, "\n", "The first 20 bases are", "\n", first_20)


