from math import factorial

def binomial(n,k):
	return factorial(n) / (factorial(k) * factorial(n - k))

def main():
	f = open('/Volumes/Data/nick/Downloads/rosalind_pper.txt', 'r')

	[n, k] = map(int, f.readline().split('\n')[0].split(' '))

	f.close()

	print ( binomial(n, k) * factorial(k) ) % 1000000

	return

if __name__ == '__main__':
	main()