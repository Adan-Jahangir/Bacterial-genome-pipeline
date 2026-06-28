from Bio import SeqIO
import os

print("REAL AMR PIPELINE STARTED")

folder = "genomes"

# real AMR gene "signatures" (simplified learning version)
amr_genes = ["blaTEM", "blaCTX", "tetA", "sul1", "mecA"]

files = os.listdir(folder)

for file in files:
    path = os.path.join(folder, file)

    sequence = ""

    for record in SeqIO.parse(path, "fasta"):
        sequence += str(record.seq)

    found_genes = []

    for gene in amr_genes:
        if gene in sequence:
            found_genes.append(gene)

    print("\nGenome:", file)
    print("Length:", len(sequence))
    print("AMR Genes Found:", found_genes if found_genes else "None")

print("\nDONE")