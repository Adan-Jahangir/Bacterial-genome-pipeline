from Bio import SeqIO
import os
import matplotlib.pyplot as plt

print("STEP 10: VISUALIZATION STARTED")

folder = "genomes"

names = []
lengths = []
gc_values = []

for file in os.listdir(folder):
    path = os.path.join(folder, file)

    sequence = ""

    for record in SeqIO.parse(path, "fasta"):
        sequence += str(record.seq)

    length = len(sequence)
    gc = round((sequence.count("G") + sequence.count("C")) / length * 100, 2)

    names.append(file)
    lengths.append(length)
    gc_values.append(gc)

print("\nDATA READY")

# ---------------- GRAPH 1 ----------------
plt.figure(figsize=(8,5))
plt.bar(names, lengths)
plt.title("Genome Length Comparison")
plt.xticks(rotation=30)
plt.tight_layout()

# save instead of only show
plt.savefig("results/genome_length.png")

# ---------------- GRAPH 2 ----------------
plt.figure(figsize=(8,5))
plt.bar(names, gc_values)
plt.title("GC Content Comparison")
plt.xticks(rotation=30)
plt.tight_layout()

# save instead of only show
plt.savefig("results/gc_content.png")

print("\nDONE - graphs saved in results folder")