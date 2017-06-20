# Project Rosalind
# June 20, 2017
# Luiz Franca
# Problem 03
# REVC

import sys

entry = sys.stdin.read()

solution = ""

for i in entry[::-1]:
	if i == "T":
		solution += "A"
	elif i == "A":
		solution += "T"
	elif i == "G":
		solution += "C"
	else:
		solution += "G"

print solution
