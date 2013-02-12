def import_fasta_data():
	# open the text file
	f = open('/Volumes/Data/nick/Downloads/rosalind_grph.txt', 'r')

	lines = f.readlines()

	# close the text file
	f.close()
	
	# a dictionary of fasta lines
	fasta_dic = {}

	# for each line
	for i in range(len(lines)):
		cleanLine = lines[i].split('\n')[0]
		
		if cleanLine[0] == '>':
			fasta = cleanLine[1:]
			j = 1
			fasta_string = []
			while j + i < len(lines) and lines[i+j][0] != '>':
				fasta_string.append(lines[i+j].split('\n')[0])
				j += 1
			fasta_string = ''.join(fasta_string)

		fasta_dic[fasta] = fasta_string

	return fasta_dic

def main():
	# read in the FASTA data into a dictionary
	fasta_data = import_fasta_data()

	# for each fasta (name, string) tuple
	for (name, string) in fasta_data.items():
		# get the end of the string
		end_of_string = string[-3:]
		
		# compare with each other to see if there is a match
		for (name_others, string_others) in fasta_data.items():
			# don't compare the string to itself
			if (name_others != name) and end_of_string == string_others[0:3]:
				# print 'Matched %s and %s' % (name, name_others)
				print '%s %s' % (name, name_others)

if __name__ == '__main__':
	main()