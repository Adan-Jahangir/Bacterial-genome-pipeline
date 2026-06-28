sequence = "ATGCGCGATCGATCGATCGCGCGATATATATGCGCGCGATCGATCGCGC"

print("Length:", len(sequence))

g = sequence.count("G")
c = sequence.count("C")

gc = (g + c) / len(sequence) * 100
print("GC Content:", round(gc, 2), "%")