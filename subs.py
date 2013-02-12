import re, string

def main():
	f = open('/Volumes/Data/nick/Downloads/rosalind_subs.txt', 'r')
	# f = open('test.txt')

	long_string = f.read()

	s = long_string.split('\n')[0]
	t = long_string.split('\n')[1]

	comp = re.compile('(?=' + t + ')')

	print s
	
	res = re.finditer(comp, s)

	locations = []

	for i in res:
		locations.append(str(i.start() + 1))

	print string.join(locations)

	f.close()

if __name__ == '__main__':
	main()