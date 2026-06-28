from Bio import SeqIO

for record in SeqIO.parse("genome.fasta", "fasta"):
    sequence = record.seq

    print("ID:", record.id)
    print("Length:", len(sequence))