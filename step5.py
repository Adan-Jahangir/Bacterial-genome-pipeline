from Bio import SeqIO

# fake AMR gene signatures (just for practice)
resistance_signatures = ["ATGCG", "CGTAC", "TTGAA"]

folder_files = [
    "genomes/ecoli.fasta",
    "genomes/Klebsiella pneumoniae.fasta",
    "genomes/Pseudomonas aeruginosa.fasta"
]

for file in folder_files:
    sequence = ""

    for record in SeqIO.parse(file, "fasta"):
        sequence += str(record.seq)

    found_genes = []

    for gene in resistance_signatures:
        if gene in sequence:
            found_genes.append(gene)

    print("\nFile:", file)
    print("Length:", len(sequence))

    if found_genes:
        print("AMR signals found:", found_genes)
    else:
        print("AMR signals found: None")