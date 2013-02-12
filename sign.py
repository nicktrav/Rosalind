import math, numpy, itertools

def main():
	# open the file
	f = open('/Volumes/Data/nick/Downloads/rosalind_sign.txt', 'r');

	n = int(f.readline().split('\n')[0])

	# close the file
	f.close()

	signed_perms = int(math.pow(2,n) * math.factorial(n))

	# generate the initial permuations
	init_permutations = numpy.array(list(itertools.permutations(numpy.array(range(1,n+1)))))

	#generate the permuation vectors
	perm_vectors = numpy.array(list(itertools.product([1,-1], repeat = n)))

	all_perms = []
	for i in init_permutations:
		for j in perm_vectors:
			all_perms.append(i * j)

	print signed_perms
	for i in all_perms:
		print ' '.join(map(str,i))

	return


if __name__ == '__main__':
	main()