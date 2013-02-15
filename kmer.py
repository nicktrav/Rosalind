import re
import itertools

# return all k-mers of length k
def all_k_mers(k):
	l = []
	for i in itertools.product('ACGT', repeat=4):
		# print i
		l.append(''.join(list(i)))

	return l

# for a string, s, return all k-mers
def find_k_mers(s, k):
	n = len(s)
	k_mers = []
	for i in range(n - k + 1):
		k_mers.append(s[i:i+4])

	return k_mers

# for a string, s, and a given k-mer, return the number of times it appears
def k_mer_count(s, k_mer):
	res = re.finditer('(?=' + k_mer + ')', s)
	
	count = 0
	for i in res:
		count += 1

	return count


def remove_duplicates(seq):
    seen = set()
    seen_add = seen.add
    return [ x for x in seq if x not in seen and not seen_add(x)]

def main():
	# import the FASTA string from file
	f = open('/Volumes/Data/nick/Downloads/rosalind_kmer.txt', 'r')

	s = ''.join(f.read().split('\n')[1:])

	f.close()

	all_kmers = all_k_mers(4)
	# print len(all_kmers)

	# return

	# define k
	k = 4

	# the length of the string
	n = len(s)

	# the number of k-mers
	n_k_mers = n - k + 1

	# find all the k_mers
	k_mers = find_k_mers(s, k)

	# remove duplicates
	k_mers_no_dup = remove_duplicates(k_mers)

	#sort the k_mers
	k_mers_no_dup.sort()
	# print k_mers_no_dup

	# for each k-mer, do a count
	k_mer_comp = []
	for k_mer in all_kmers:
		# print k_mer
		k_mer_comp.append(k_mer_count(s, k_mer))

	print ' '.join(map(str, k_mer_comp))

	return

if __name__ == '__main__':
	main()