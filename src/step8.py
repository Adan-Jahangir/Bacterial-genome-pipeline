from Bio import SeqIO
import os

print("STEP 8: SEQUENCE-BASED AMR SIMULATION")

folder = "genomes"

# small DNA motifs (simulate real resistance fragments)
amr_motifs = [
    "ATGCGT",
    "CGTACG",
    "TTGAC",
    "GGCATA",
    "TTCGAA"
]

files = os.listdir(folder)

for file in files:
    path = os.path.join(folder, file)

    sequence = ""

    for record in SeqIO.parse(path, "fasta"):
        sequence += str(record.seq)

    found = []

    for motif in amr_motifs:
        if motif in sequence:
            found.append(motif)

    print("\nGenome:", file)
    print("Length:", len(sequence))
    print("Motif matches:", found if found else "None")

print("\nDONE")