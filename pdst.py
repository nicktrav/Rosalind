import itertools
import numpy as np

def hamming_dist(s1, s2):
	n = len(s1)

	diff = 0.
	for i in range(n):
		if s1[i] != s2[i]:
			diff += 1

	return diff / n

def main():
	# read the data from file
	f = open('/Volumes/Data/nick/Downloads/rosalind_pdst.txt', 'r')

	lines = f.read().split('\n')[:-1]

	f.close()

	start_lines = []
	for i in range(len(lines)):
		if lines[i][0] == '>':
			start_lines.append(i)

	line_len = start_lines[1]

	s = []
	for start in start_lines:
		s.append(''.join(lines[start+1:start+line_len]))

	# a set of tuples to compare
	comparisons = itertools.combinations(range(len(s)), 2)

	# initialise the matrix D
	D = np.zeros((len(s), len(s)))

	# for each pair of strings
	for pair in comparisons:
		# compute the Hamming distance
		dist = hamming_dist(s[pair[0]], s[pair[1]])
		# set the relevant values in the matrix
		D[pair[0], pair[1]] = dist
		D[pair[1], pair[0]] = dist

	# formatted output
	for i in range(len(s)):
		l = ''
		for j in range(len(s)):
			l += '%.5f ' % D[i, j]
		print l

	return

if __name__ == '__main__':
	main()