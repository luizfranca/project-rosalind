# Project Rosalind
# June 22, 2017
# Luiz Franca
# Problem 09
# SUBS

import sys

dna_string = sys.stdin.readline().replace("\n", "")
dna_sub = sys.stdin.readline().replace("\n", "")

indexes = []
for i in range(0, len(dna_string)):
	if dna_string[i : i + len(dna_sub)] == dna_sub:
		indexes.append(str(i + 1))

print " ".join(indexes)
