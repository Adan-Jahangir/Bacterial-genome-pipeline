from Bio import SeqIO
import os

folder = "genomes"

files = os.listdir(folder)

for file in files:
    path = os.path.join(folder, file)

    sequence = ""

    for record in SeqIO.parse(path, "fasta"):
        sequence += str(record.seq)

    g = sequence.count("G")
    c = sequence.count("C")

    gc = (g + c) / len(sequence) * 100

    print(file)
    print("Length:", len(sequence))
    print("GC%:", round(gc, 2))
    print("------")