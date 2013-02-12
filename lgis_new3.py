#!/usr/bin/env python

""" Rosalind project - Problem: Longest Increasing Subsequence
Problem
A subsequence of a permutation is a collection of elements of the permutation in the order
that they appear. For example, (5, 3, 4) is a subsequence of (5, 1, 3, 4, 2).
A subsequence is increasing if the elements of the subsequence increase, and decreasing if
the elements decrease. For example, given the permutation (8, 2, 1, 6, 5, 7, 4, 3, 9), an
increasing subsequence is (2, 6, 7, 9), and a decreasing subsequence is (8, 6, 5, 4, 3).
You may verify that these two subsequences are as long as possible.

Given: A positive integer n<=10000 followed by a permutation Pi of length n.
Return: A longest increasing subsequence of Pi, followed by a longest decreasing subsequence
of Pi.

Sample Dataset
5
5 1 4 2 3
Sample Output
1 2 3
5 4 2

Citation
Adapted from Jones & Pevzner, *An Introduction to Bioinformatics Algorithms, Problem 6.48.
"""

__author__ = "Daniel J. Barnes"
__email__ = "ghen2000@gmail.com"
__status__ = "Working"

"""
Major sources:
algo: 		http://en.wikipedia.org/wiki/Longest_increasing_subsequence#Efficient_algorithms
debugging:	http://stackoverflow.com/questions/3992697/longest-increasing-subsequence
"""

import sys

def long_inc_sseq(seq):
	seq = [None] + seq
	n = len(seq)
	M = [None] * n
	P = [None] * n
	L = 0

	for i in range(1,n):
		if L == 0 or seq[M[1]] >= seq[i]:
			j = 0
		else:
			low = 1
			hi = L + 1
			while low < hi - 1:
				mid = (hi + low) // 2
				if seq[M[mid]] < seq[i]:
					low = mid
				else:
					hi = mid
			j = low

		P[i] = M[j]

		if j == L or seq[i] < seq[M[j+1]]:
			M[j+1] = i
			L = max(L, j+1)

	res = []
	pos = M[L]
	while L > 0:
		res.append(seq[pos])
		pos = P[pos]
		L -= 1

	return res[::-1]


if sys.argv[1] == "-i":
	filein = open(sys.argv[2], 'r')
	lines = filein.read().splitlines()
	filein.close
else:
	lines = sys.argv[1]

n = lines[0]
seq = [int(x) for x in lines[1].split()]

inc = long_inc_sseq(seq)
seq.reverse()
dec = long_inc_sseq(seq)
dec.reverse()

inc = [str(x) for x in inc]
dec = [str(x) for x in dec]

out = ' '.join(inc)+'\n'+' '.join(dec)

fileout = open('LGIS_output.txt','w')
fileout.write(out)						# writes to file, closes file, and rereads file
fileout.close 							# to make sure the output is correct in the file
fileout = open('LGIS_output.txt','r')
print fileout.read()
fileout.close