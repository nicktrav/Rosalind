def construct_mass_table():
	# open the text file
	f = open('monoisotopic_mass_table.txt', 'r')

	mass_table = {}

	for line in f.readlines():
		pair = line.split('\n')[0].split('   ')
		mass_table[pair[0]] = float(pair[1])

	# close the file
	f.close()

	mass_table['water'] = 18.01056

	return mass_table

def main():
	# load the mass table
	mass_table = construct_mass_table()

	# open the file
	f = open('/Volumes/Data/nick/Downloads/rosalind_prtm.txt', 'r')

	protein_string = list(f.readline().split('\n')[0])

	# close the file
	f.close()

	protein_weight = 0.0

	# for each amino acid in the protein, add its weight to the sum
	for acid in protein_string:
		protein_weight += mass_table[acid]

	print protein_weight

	return

if __name__ == '__main__':
	main()