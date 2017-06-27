# Project Rosalind
# June 27, 2017
# Luiz Franca
# Problem 10
# FIBD

import sys

def fib(n, m):
	rabbits = [1] + [0] * (m - 1)

	for k in xrange(n - 1):
		new_borns = 0
		
		for i in range(m - 1, 0, -1):
			if (i != 0):
				new_borns += rabbits[i]
				
			rabbits[i] = rabbits[i-1]
			

		rabbits[0] = new_borns

	return sum(rabbits)

n, m = map(lambda x: int(x), sys.stdin.read().split())

print fib(n, m)