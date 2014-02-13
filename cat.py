CAT_LIST = {0:1, 1:1}
def catalan(n):
	"""Return the n-th catalan number"""
	
	# if the number is already in the dictionary, return it
	if n in CAT_LIST:
		return CAT_LIST[n]

	# otherwise, recursively compute it
	s = 0
	for k in range(1, n+1):
		s += catalan(k - 1) * catalan(n - k)

	CAT_LIST[n] = s
	return CAT_LIST[n]


def main():
	# import file for reading
	f = open('/Users/nick/Downloads/rosalind_cat.txt', 'r')

	# read file
	lines = f.readlines()

	# close file 
	f.close()

if __name__ == '__main__':
	main()