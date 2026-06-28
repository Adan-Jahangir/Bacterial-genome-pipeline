\# AMR Genome Analysis Pipeline



\## What this project does



This project analyzes bacterial genome FASTA files and extracts:



\- Genome length

\- GC content

\- k-mer based pattern analysis

\- Simple AMR risk scoring (simulation)

\- Visual graphs and CSV reports



\---



\## How to run



\### 1. Install dependencies

pip install -r requirements.txt



\### 2. Add genomes

Place FASTA files inside:

genomes/



\### 3. Run pipeline

py src/pipeline.py



\### 4. Check results

All outputs appear in:

results/



\---



\## Output includes



\- CSV report of genome statistics

\- GC content graph

\- Genome length graph

\- AMR risk score visualization



\---



\## Note



This is a bioinformatics learning project.

It demonstrates genome parsing, k-mer analysis, and basic comparative genomics.

