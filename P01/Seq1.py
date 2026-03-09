from pathlib import Path

class Seq:

    def __init__(self, strbases = None):
        if strbases == None:
            self.bases = "NULL"
            print("Null sequence created")
        else:
            valid = True
            valid_bases = ["A", "C", "T", "G"]
            for base in strbases:
                if valid and base not in valid_bases:
                    valid = False
            if valid:
                self.bases = strbases
                print("New sequence created!")
            else:
                self.bases = "ERROR"
                print("Invalid sequence created")

    def __str__(self):
        return self.bases

    def len(self):
        if self.bases == "NULL" or self.bases == "ERROR":
            length = 0
        else:
            length = len(self.bases)
        return length

    def count_base(self, base):
        if self.bases == "NULL" or self.bases == "ERROR":
            count = 0
        else:
            count = 0
            for b in self.bases:
                if b == base:
                    count += 1
        return count


    def count(self):
        dict = {"A":0,"C":0,"G":0,"T":0}
        if self.bases == "NULL" or self.bases == "ERROR":
            pass
        else:
            list_bases = ["A","C","G","T"]
            for base in list_bases:
                count = 0
                for a in self.bases:
                    if a == base:
                        count += 1
                dict.update({base:count})
        return dict

    def reverse(self):
        if self.bases == "NULL" or self.bases == "ERROR":
            result = self.bases
        else:
            result = self.bases[::-1]
        return result

    def complement(self):
        if self.bases == "NULL" or self.bases == "ERROR":
            result = self.bases
        else:
            compliment_dict = {"A": "T", "T": "A", "C": "G", "G": "C"}
            new_seq = ""
            for base in self.bases:
                new_seq += compliment_dict[base]
            result = new_seq
        return result

    def read_fasta(self,filename):
        file_contents = Path(filename).read_text()
        non_header = file_contents.split("\n")[1:-1]
        self.bases = "".join(non_header)
        return self.bases


