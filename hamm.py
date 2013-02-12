from string import maketrans

def main():
	# open the file for reading
	f = open('/Volumes/Data/nick/Downloads/rosalind_hamm.txt', 'r');

	# read the first string, 's'
	s = list(f.readline());
	# strip the newline character
	s = s[0:-1]
	# read the second string, 't'
	t = list(f.readline());

	# the length of the two DNA strings
	stringLen = len(s);

	# the Hamming distance (init 0)
	dH = 0;

	for i in range(stringLen):
		if s[i] != t[i]:
			dH = dH + 1

	print dH

	# close the file
	f.close();

if __name__ == '__main__':
	main()