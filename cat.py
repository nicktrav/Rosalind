def main():
	# import file for reading
	f = open('/Users/nick/Downloads/rosalind_cat.txt', 'r')

	# read file
	lines = f.readlines()

	# close file 
	f.close()

if __name__ == '__main__':
	main()