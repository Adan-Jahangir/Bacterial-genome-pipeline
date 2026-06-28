from Bio import SeqIO
import os

print("STEP 9: GENOME SIMILARITY (K-MER ANALYSIS)")

folder = "genomes"

def get_kmers(sequence, k=3):
    kmers = []
    for i in range(len(sequence) - k + 1):
        kmers.append(sequence[i:i+k])
    return set(kmers)

genomes = {}

# load genomes
for file in os.listdir(folder):
    path = os.path.join(folder, file)

    sequence = ""

    for record in SeqIO.parse(path, "fasta"):
        sequence += str(record.seq)

    genomes[file] = get_kmers(sequence)

# compare genomes
files = list(genomes.keys())

for i in range(len(files)):
    for j in range(i + 1, len(files)):

        g1 = files[i]
        g2 = files[j]

        set1 = genomes[g1]
        set2 = genomes[g2]

        intersection = len(set1 & set2)
        union = len(set1 | set2)

        similarity = round((intersection / union) * 100, 2)

        print(f"{g1} vs {g2} → {similarity}% similarity")

print("\nDONE")