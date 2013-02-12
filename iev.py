def main():
	# open the text file
	txt = open('/Volumes/Data/nick/Downloads/rosalind_iev.txt', 'r')

	# read in the values
	[a, b, c, d, e, f] = map(float, txt.readline().split('\n')[0].split(' '))

	# close the file
	txt.close()	

	expected = 2 * (a + b + c + (0.75 * d) + (0.5 * e))
	print expected

if __name__ == '__main__':
	main()