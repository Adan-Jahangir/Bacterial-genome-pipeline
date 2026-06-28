from Bio import SeqIO
import os
import csv

print("STEP 11: FINAL REPORT GENERATION")

folder = "genomes"
output_file = "results/amr_summary.csv"

rows = []

for file in os.listdir(folder):
    path = os.path.join(folder, file)

    sequence = ""

    for record in SeqIO.parse(path, "fasta"):
        sequence += str(record.seq)

    length = len(sequence)
    gc = round((sequence.count("G") + sequence.count("C")) / length * 100, 2)

    rows.append([file, length, gc])

# write CSV report
with open(output_file, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Genome", "Length", "GC_Content"])
    writer.writerows(rows)

print("\nREPORT SAVED:", output_file)

for r in rows:
    print(r)

print("\nDONE")