# Project Rosalind
# June 20, 2017
# Luiz Franca
# Problem 05
# DNA

import sys

def gc_content(sequence):
	return (sequence.count("G") + sequence.count("C")) / float(len(sequence))


curr_label = ""
curr_sequence = ""
curr_score = 0

best_label = ""
best_sequence = ""
best_score = 0

for line in sys.stdin.readlines():
	line = line.replace("\n", "")

	if line[0] != ">":
		curr_sequence += line
	else:
		if curr_sequence != "":

			curr_score = gc_content(curr_sequence)

			if curr_score > best_score:
				best_label = curr_label
				best_sequence = curr_sequence
				best_score = curr_score

		curr_sequence = ""
		curr_score = 0

		curr_label = line[1:]
else:
	curr_score = gc_content(curr_sequence)

	if curr_score > best_score:
		best_label = curr_label
		best_sequence = curr_sequence
		best_score = curr_score
		


print best_label
print best_score * 100