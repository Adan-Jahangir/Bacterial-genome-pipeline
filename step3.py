from Bio import SeqIO

sequence = ""

for record in SeqIO.parse("genome.fasta", "fasta"):
    sequence += str(record.seq)

print("Genome Length:", len(sequence))

g = sequence.count("G")
c = sequence.count("C")

gc = (g + c) / len(sequence) * 100
print("GC Content:", round(gc, 2), "%")