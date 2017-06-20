# Project Rosalind
# Luiz França
# Problem 01
# DNA

import sys

entry = sys.stdin.read()

print "%d %d %d %d" % (entry.count("A"), entry.count("C"), entry.count("G"), entry.count("T"))