import itertools

# define the global variable symbols
symbols = []

def cmpFunc(x, y):
	# for the case where they are equal
	if x == y:
		return 0

	# for the case where x and y are the same length
	# defualt assumption that x > y
	if len(x) == len(y):
		for i in range(len(x)):
			if symbols.index(x[i]) < symbols.index(y[i]):
				return -1
			if symbols.index(x[i]) > symbols.index(y[i]):
				return 1
		# return 1

	# for the case where len(x) < len(y)
	# assume that x > y
	if len(x) < len(y):
		for i in range(len(x)):
			if symbols.index(x[i]) < symbols.index(y[i]):
				return -1
			if symbols.index(x[i]) > symbols.index(y[i]):
				return 1
		return -1

	# for the case where len(y) < len(x)
	# assume that x > y
	if len(y) < len(x):
		for i in range(len(y)):
			if symbols.index(y[i]) > symbols.index(x[i]):
				return -1
			if symbols.index(y[i]) < symbols.index(x[i]):
				return 1
		return 1


def main():
	# open the file
	f = open('/Volumes/Data/nick/Downloads/rosalind_lexv.txt', 'r');

	# read the symbols
	global symbols
	symbols = f.readline().split('\n')[0].split(' ')
	# read the integer
	n = int(f.readline().split('\n')[0])

	# close the file
	f.close()

	# generate all the permuations of length n
	all_perms = []
	for i in range(1,n+1):
		perms = itertools.product(symbols, repeat = i)
		all_perms.extend(perms)

	A = []
	for i in all_perms:
		A.append(''.join(i))

	# sort the list
	# A = ['A', 'AB']
	all_perms_sorted = sorted(all_perms, cmp=cmpFunc)

	for i in all_perms_sorted:
		print ''.join(i)

if __name__ == '__main__':
	main()