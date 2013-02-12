def construct_lookup():
	# open the file
	f = open('prot_lookup.txt', 'r')

	# for each line in the file, add the tuple to the dictionary
	lines = f.readlines()

	# close the file
	f.close()
	
	# define the empty lookup table
	lookup = {}
	
	# add each (codon, acid) pair to the lookup table
	for line in lines:
		(codon, acid) = line.split('\n')[0].split(' ')
		lookup[codon] = acid

	# return the lookup table
	return lookup

def main():
	# construct the lookup table
	lookup = construct_lookup()

	# open the text to be translated
	f = open('/Volumes/Data/nick/Downloads/rosalind_prot.txt', 'r')
	
	# get the rna string
	rna_string = f.readline().split('\n')[0]
	
	# close the file
	f.close()

	# the number of translations to do
	iterations = len(rna_string) / 3

	# the empty proteins string 
	prot_string = []
	
	for i in range(0, len(rna_string), 3):
		# print 'translating: [%s]' % rna_string[i:i+3]
		# print '\t -> %s' % lookup[rna_string[i:i+3]]
		acid = lookup[rna_string[i:i+3]]
		prot_string.append(acid)

	print ''.join(prot_string[:-1])

if __name__ == '__main__':
	main()