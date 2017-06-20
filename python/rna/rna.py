# Project Rosalind
# Luiz França
# Problem 02
# RNA

import sys

entry = sys.stdin.read()

print "".join(map(lambda x : "U" if x == "T" else x, entry))