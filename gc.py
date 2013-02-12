def create_FASTA_dict():
	# open the file for reading
	f = open('/Volumes/Data/nick/Downloads/rosalind_gc.txt', 'r');

	#read in the whole file
	s = f.read()

	#split the string into substrings of names and dna strings
	pairs = s.split('>')[1:];

	# define a new dictionary
	d = {};

	# extract the name and the dna string
	for pair in pairs:
		FASTA_name = pair.split('\n')[0];
		dna_string = ''.join(pair.split('\n')[1:]);
		
		# add to the dictionary with gc count 0
		d[FASTA_name] = [dna_string, 0];

	return d;

def compute_gc(s):
	return (s.count('G') + s.count('C')) / float(len(s));

def main():
	d = create_FASTA_dict();

	high_gc_FASTA = '';
	high_gc = 0;

	for key in d.keys():
		res = compute_gc(d[key][0]);
		d[key][1] = res;

		if res > high_gc:
			high_gc_FASTA = key;
			high_gc = res;

	print high_gc_FASTA;
	print '%.6f%%' % (high_gc * 100);

if __name__ == '__main__':
	main()