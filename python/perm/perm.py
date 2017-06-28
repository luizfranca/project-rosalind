# Project Rosalind
# June 27, 2017
# Luiz Franca
# Problem 11
# PERM

import sys

m = int(sys.stdin.read())


def permute(init, perm, depth):
	if depth == 0:
		return perm
	
	for i in range(len(init) - 1):
		new_element = []
		for j in range(i + 1, len(init)):
			# print i, j
			new_element = init[:]
			new_element[i], new_element[j] = new_element[j], new_element[i]
			if (not new_element in perm):
				perm.append(new_element)
			permute(new_element, perm, depth - 1)

	return perm
	

init = range(1, m + 1)

perm = permute(init, [init], m)

print len(perm)

for line in perm:
	print " ".join(map(lambda x : str(x), line))