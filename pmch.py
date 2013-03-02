import math

def main():
	# load data from file
	f = open('/Volumes/Data/nick/Downloads/rosalind_pmch.txt', 'r')

	s = ''.join(f.read().split('\n')[1:])

	f.close()

	# print s
	# return

	# length of the string (should be even)
	n = len(s) / 2
	
	# count the GC pairs
	GCcount = s.count('G')
	print GCcount

	# count the AU pairs
	AUcount = s.count('A')
	print AUcount

	print math.factorial(GCcount) * math.factorial(AUcount)

	return

if __name__ == '__main__':
	main()