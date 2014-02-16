import re

def format_output(s):
	'''Format the output for Rosalind'''
	o = '{'

	o += ', '.join(list(map(str, s)))

	o += '}'

	return o

def main():
	# load the file
	f = open('/Users/nick/Downloads/rosalind_seto.txt', 'r')

	# read the lines of the file
	lines = f.readlines()

	# close the file
	f.close()

	# define variables
	n = int(lines[0].split('\n')[0])

	res = re.findall(r'[\d]+', lines[1])
	A = frozenset(map(int, res))

	res = re.findall(r'[\d]+', lines[2])
	B = frozenset(map(int, res))

	U = frozenset(range(1, n+1))

	# union
	o1 = A | B

	# instersection
	o2 = A & B

	# A - B
	o3 = A - B

	# B - A
	o4 = B - A

	# U - A
	o5 = U - A

	# U - B
	o6 = U - B

	for o in [o1, o2, o3, o4, o5, o6]:
		print format_output(o)

if __name__ == '__main__':
	main()