import itertools, math

def main():
	f = open('/Volumes/Data/nick/Downloads/rosalind_perm.txt', 'r');

	n = int(f.readline().split('\n')[0])

	f.close()

	s = ''.join(map(str, range(1,n+1)))

	print math.factorial(n)

	for i in itertools.permutations(s):
		print ' '.join(i)

if __name__ == '__main__':
	main()