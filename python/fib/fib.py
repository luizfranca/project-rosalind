# Project Rosalind
# June 20, 2017
# Luiz Franca
# Problem 04
# FIB

import sys

def fib(n, k):
	fcurr = 1
	fpast = 1
	
	if n <= 2:
		return 1

	for i in xrange(n - 2):
		fpast, fcurr = fcurr, fcurr + fpast * k

	return fcurr

n, k = map(lambda x: int(x), sys.stdin.read().split())

print fib(n, k)