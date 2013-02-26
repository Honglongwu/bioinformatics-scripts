from Bio import SeqIO

(file, id, start, end) = ("secondround_merged_expanded.fasta", "C7136661:0-107", 1, 10)

record_dict = SeqIO.index(file, "fasta")
print record_dict[id].seq[start:end]
