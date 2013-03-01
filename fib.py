def rabbits(n, k):
	if n == 1 or n == 2:
		return 1
	else:
		return rabbits(n-1, k) + k * rabbits(n - 2, k)


def main():
	# read in information from file
	f = open('/Volumes/Data/nick/Downloads/rosalind_fib.txt', 'r')

	[n, k] = map(int, f.readline().split(' '))

	f.close()

	print rabbits(n, k)

if __name__ == '__main__':
	main()