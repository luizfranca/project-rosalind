# Project Rosalind
# June 20, 2017
# Luiz Franca
# Problem 06
# HAMM

import sys

s = sys.stdin.readline().replace("\n", "")
t = sys.stdin.readline().replace("\n", "")

print sum([1 if s[i] != t[i] else 0 for i in range(len(s))])