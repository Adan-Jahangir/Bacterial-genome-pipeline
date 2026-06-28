print("PIPELINE STARTED")

from Bio import SeqIO
import csv
import os

folder = "genomes"

amr_patterns = ["ATGCG", "CGTAC", "TTGAA"]

files = os.listdir(folder)

print("Found files:", files)

results = []

for file in files:
    path = os.path.join(folder, file)

    sequence = ""

    for record in SeqIO.parse(path, "fasta"):
        sequence += str(record.seq)

    length = len(sequence)

    gc = round((sequence.count("G") + sequence.count("C")) / length * 100, 2)

    found = [p for p in amr_patterns if p in sequence]

    print("\nProcessing:", file)
    print("Length:", length)
    print("GC:", gc)
    print("AMR hits:", found)

    results.append([file, length, gc, len(found)])

with open("results/amr_results.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Genome", "Length", "GC_Content", "AMR_Signals"])
    writer.writerows(results)

print("\nDONE")