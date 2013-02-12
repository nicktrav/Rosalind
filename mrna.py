def main():
	f = open('/Volumes/Data/nick/Downloads/rosalind_mrna.txt', 'r')

	s = list(f.readline().split('\n')[0])

	f.close()

	reverse_lookup = {'F': 2, 'L': 6, 'S': 6, 'Y': 2, 'Stop': 3, 'C': 2, 'W': 1, 'P': 4, 'H': 2, 'Q': 2, 'R': 6, 'I': 3, 'M': 1, 'T': 4, 'N': 2, 'K': 2, 'V': 4, 'A': 4, 'D': 2, 'E': 2, 'G': 4}

	total = 1
	for i in s:
		total = (total * reverse_lookup[i]) % 1000000

	total = (total * reverse_lookup['Stop']) % 1000000

	print total

if __name__ == '__main__':
	main()