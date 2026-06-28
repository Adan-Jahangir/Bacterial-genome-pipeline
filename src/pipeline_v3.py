from Bio import SeqIO
import os
import csv
import matplotlib.pyplot as plt

print("AMR PIPELINE v3 STARTED")

folder = "genomes"

# weighted k-mer style AMR signals (simulation of resistance bias regions)
amr_signals = {
    "ATG": 1,
    "CGT": 1,
    "GGC": 2,
    "TTA": 1,
    "CGA": 2
}

names = []
lengths = []
gc_values = []
amr_scores = []

rows = []

for file in os.listdir(folder):
    path = os.path.join(folder, file)

    sequence = ""

    for record in SeqIO.parse(path, "fasta"):
        sequence += str(record.seq)

    length = len(sequence)
    gc = round((sequence.count("G") + sequence.count("C")) / length * 100, 2)

    # -------------------------
    # AMR SCORE (weighted k-mer enrichment)
    # -------------------------
    score = 0
    for kmer, weight in amr_signals.items():
        count = sequence.count(kmer)
        score += count * weight

    # normalize score per million bases
    normalized_score = round((score / length) * 1_000_000, 2)

    names.append(file)
    lengths.append(length)
    gc_values.append(gc)
    amr_scores.append(normalized_score)

    rows.append([file, length, gc, normalized_score])

    print(f"{file}")
    print(f"  Length: {length}")
    print(f"  GC%: {gc}")
    print(f"  AMR Risk Score: {normalized_score}\n")

# -------------------------
# SAVE REPORT
# -------------------------
with open("results/amr_report_v3.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Genome", "Length", "GC_Content", "AMR_Risk_Score"])
    writer.writerows(rows)

# -------------------------
# PLOT AMR RISK
# -------------------------
plt.figure()
plt.bar(names, amr_scores)
plt.title("AMR Risk Score (Normalized)")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("results/amr_risk_v3.png")

print("PIPELINE v3 COMPLETE")