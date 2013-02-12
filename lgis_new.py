import itertools

def generate_increasing_subsequence(l, start):
	subsequence = [l[start]]
	
	for i in range(start, len(l)-1):
		if l[i+1] > subsequence[-1]:
			subsequence.append(l[i+1])

	return subsequence

def main():
	# import file
	f = open('/Volumes/Data/nick/Downloads/rosalind_lgis.txt', 'r')

	lines = f.read().split('\n')

	f.close()

	n = int(lines[0])
	pi = map(int, lines[1].split(' '))

	for i in range(n):
		print generate_increasing_subsequence(pi, i)

if __name__ == '__main__':
	main()