def recursive_reduce(s):
	"""Recursively eliminate all isolated pairs.
	Do this until there are no isolated pairs remaining."""

	# initial isolation
	r = isolate_pairs(s)

	# if no isolated pairs remain, return what is left
	if len(r) == 0:
		return s

	# otherwise, remove the bases at the defined locations
	s_list = list(s)
	for pair in r:
		s_list[pair[0]] = ''
		s_list[pair[1]] = ''

	return recursive_reduce(''.join(s_list))

def isolate_pairs(s):
	"""Is this an 'isolated pair?"""
	# a list of isolated pairs
	pairs = []

	for i in range(len(s)):
		# definition of an isolated pair
		if (match(s[i], s[(i+1) % len(s)]) == True) and (match(s[(i+1) % len(s)], s[(i+2) % len(s)]) == False) and (match(s[i], s[(i-1) % len(s)]) == False):
			# add to the list of isolated pairs
			pairs.append((i,(i+1) % len(s)))

	# return the list
	return pairs

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

	print recursive_reduce(s)

if __name__ == '__main__':
	main()