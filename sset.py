import itertools, math

def combinations(n, k):
	return math.factorial(n) / (math.factorial(k) * math.factorial(n - k))

def main():

	# import the string from file
	f = open('/Volumes/Data/nick/Downloads/rosalind_sset.txt', 'r')

	n = int(f.readline().split('\n')[0])
	f.close()

	# account for the empty set
	count = 1
	for i in range(1,n+1):
		count += combinations(n, i)

	print count % 1000000

if __name__ == '__main__':
	main()