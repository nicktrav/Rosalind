# load the reads in from file
def load_reads(f):
	f = open(f, 'r')

	lines = f.read().split('\n')[:-1]

	f.close()

	start_lines = []
	for i in range(len(lines)):
		if lines[i][0] == '>':
			start_lines.append(i)

	line_len = start_lines[1]

	s = []
	for start in start_lines:
		s.append(''.join(lines[start+1:start+line_len]))

	return s

# the reverse complement of a string
def reverse_complement(s):
	rc = list(s[::-1])
	for i in range(len(rc)):
		if rc[i] == 'A':
			rc[i] = 'T'
		elif rc[i] == 'C':
			rc[i] = 'G'
		elif rc[i] == 'G':
			rc[i] = 'C'		
		else:
			rc[i] = 'A'
	
	return ''.join(rc)

# find all incorrectly sequenced reads. The inverse of the set of 
# reads that appear at least twice, (may appear as reverse complement)
# returns (incorrect, correct)
def incorrectly_sequenced(reads):
	correct = []
	
	for read in reads:
		rc = reverse_complement(read)
		count = reads.count(read) + reads.count(rc)
		if count >= 2:
			correct.append(read)

	return (list(set(reads) - set(correct)), list(set(correct)))

# the hamming distance between two strings
def hamming_dist(s1, s2):
	dist = 0
	for i in range(len(s1)):
		if s1[i] != s2[i]:
			dist += 1

	return dist

# correct two strings who differ by one base pair
# s1 is the incorrect string
def correct_string(s1, s2):
	corrected = list(s2[:])
	for i in range(len(s1)):
		if s1[i] != s2[i]:
			corrected[i] = s2[i]

	return ''.join(corrected)

# find the corrections for each of the incorect reads
# reads differ in hamming distance by one to a correct read
def find_corrections(incorrect_reads, correct_reads):
	# the reverse complements of the correct reads
	rc_correct_reads = map(reverse_complement, correct_reads)

	corrections = []
	for incorrect in incorrect_reads:
		# find the hamming pair
		for correct in list(set(correct_reads) | set(rc_correct_reads)):
			if hamming_dist(incorrect, correct) == 1:
				corrections.append((incorrect, correct_string(incorrect, correct)))


	return corrections

# print a correctly formatted list of corrections
def output(corrections):
	for correction in corrections:
		print correction[0] + '->' + correction[1]

def main():
	reads = load_reads('/Volumes/Data/nick/Downloads/rosalind_corr.txt')
	# print reads

	# find all incorrectly sequenced reads
	(incorrect, correct) = incorrectly_sequenced(reads)

	# find the corrections
	corrections = find_corrections(incorrect, correct)

	# print the correctly formatted output
	output(corrections)

	return

if __name__ == '__main__':
	main()