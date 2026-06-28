from Bio import SeqIO
import csv
import os

# genomes folder
folder = "genomes"

# fake AMR patterns for now (we will replace later)
amr_patterns = ["ATGCG", "CGTAC", "TTGAA"]

results = []

for file in os.listdir(folder):
    path = os.path.join(folder, file)

    sequence = ""

    for record in SeqIO.parse(path, "fasta"):
        sequence += str(record.seq)

    length = len(sequence)

    gc = round((sequence.count("G") + sequence.count("C")) / length * 100, 2)

    found = [p for p in amr_patterns if p in sequence]

    results.append([
        file,
        length,
        gc,
        len(found)
    ])

# save output
output_file = "results/amr_results.csv"

with open(output_file, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Genome", "Length", "GC_Content", "AMR_Signals"])
    writer.writerows(results)

print("Pipeline complete → results saved in results/amr_results.csv")