import itertools

def main():
	# open the file
	f = open('/Volumes/Data/nick/Downloads/rosalind_lexf.txt', 'r');

	# read the symbols
	symbols = f.readline().split('\n')[0].split(' ')
	# read the integer
	n = int(f.readline().split('\n')[0])

	# print symbols

	# generate all the permuations of length n
	perms = itertools.product(symbols, repeat = 3)

	for i in perms: print ''.join(list(i))

	# close the file
	f.close()

if __name__ == '__main__':
	main()