from Bio import SeqIO
import os
import csv
import matplotlib.pyplot as plt

print("AMR PIPELINE STARTED\n")

folder = "genomes"
output_csv = "results/final_report.csv"

names = []
lengths = []
gc_values = []

amr_motifs = ["ATGCG", "CGTAC", "TTGAA"]

rows = []

# -------------------------
# PROCESS GENOMES
# -------------------------
for file in os.listdir(folder):
    path = os.path.join(folder, file)

    sequence = ""

    for record in SeqIO.parse(path, "fasta"):
        sequence += str(record.seq)

    length = len(sequence)
    gc = round((sequence.count("G") + sequence.count("C")) / length * 100, 2)

    motifs_found = [m for m in amr_motifs if m in sequence]

    # store for graphs
    names.append(file)
    lengths.append(length)
    gc_values.append(gc)

    # store for CSV
    rows.append([file, length, gc, len(motifs_found)])

    print(f"Processed: {file}")

# -------------------------
# SAVE CSV REPORT
# -------------------------
with open(output_csv, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Genome", "Length", "GC_Content", "AMR_Motif_Count"])
    writer.writerows(rows)

print("\nCSV REPORT SAVED")

# -------------------------
# GRAPH 1: LENGTH
# -------------------------
plt.figure()
plt.bar(names, lengths)
plt.title("Genome Length Comparison")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("results/length.png")

# -------------------------
# GRAPH 2: GC CONTENT
# -------------------------
plt.figure()
plt.bar(names, gc_values)
plt.title("GC Content Comparison")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("results/gc.png")

print("\nPIPELINE COMPLETE")
print("Results saved in /results")