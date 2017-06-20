# Project Rosalind
# June 20, 2017
# Luiz Franca
# Problem 02
# RNA

import sys

entry = sys.stdin.read()

print "".join(map(lambda x : "U" if x == "T" else x, entry))