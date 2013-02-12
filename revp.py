from operator import itemgetter

def reverse_complement(l):
	rev = l[::-1]

	rc = []
	for letter in rev:
		if letter == 'A':
			rc.append('T')
		if letter == 'C':
			rc.append('G')
		if letter == 'G':
			rc.append('C')
		if letter == 'T':
			rc.append('A')						
	
	return rc

def is_reverse_palindrome(a):
	if a == reverse_complement(a):
		return True
	else:
		return False

def main():
	# open the text file
	f = open('/Volumes/Data/nick/Downloads/rosalind_revp.txt', 'r')

	# read the string
	dna_string = list(f.readline().split('\n')[0])

	# close the file
	f.close()
	
	# a list of the palindromes to be returned
	rcs = []
	
	for n in range(4, 13):
		# find all reverse palindromes of length n
		for i in range(0,len(dna_string) - n + 1):
			if is_reverse_palindrome(dna_string[i:i+n]):
				# add the reverse palindrome to the list
				rcs.append((i+1, n))

	for i in sorted(rcs, key=itemgetter(0)):
		print '%i %i' % (i[0], i[1])

	return

if __name__ == '__main__':
	main()