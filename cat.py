def match(i, j):
	"""Are i and j conjugate pairs?"""
	return i == op(j)

MAPPING  = {'A':'U', 'U':'A', 'G':'C', 'C':'G'}
def op(x):
	"""Map a base to its conjugate"""
	if x not in MAPPING:
		print 'ERROR: not a valid character.'
		return -1

	return MAPPING[x]

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

	# the string
	s = lines[-1]	

if __name__ == '__main__':
	main()