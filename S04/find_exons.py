from pathlib import Path

exons = Path("sequences/ADA_EXONS.txt").read_text().split(">")
ada = "sequences/ADA.txt"
inverse_ada = ada[::-1]

for filthy_exon in exons:
    exon = "".join(filthy_exon.split("\n")[1:-1])
    print(exon)
    print(inverse_ada.find(exon))

string = "ada"
findin = "dakoawpodwpoadwpiodadaoqeioqpwiep"
print(findin[::-1])




print("Exon     | Long.  | Start            | End","\n",
      "-"*50,"\n",)

