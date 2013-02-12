# a function that compares two chars and returns 
# a +1 if transition, a -1 if transversion, 0 otherwise
def compare(c1, c2):
	if c1 == c2:
		return 0
	if c1 == 'A':
		if c2  == 'C':
			return -1
		elif c2 == 'G':
			return 1
		elif c2 == 'T':
			return -1
	elif c1 == 'C':
		if c2  == 'A':
			return -1
		elif c2 == 'G':
			return -1
		elif c2 == 'T':
			return 1
	elif c1 == 'G':
		if c2  == 'A':
			return 1
		elif c2 == 'C':
			return -1
		elif c2 == 'T':
			return -1
	elif c1 == 'T':  
		if c2  == 'A':
			return -1
		elif c2 == 'C':
			return 1
		elif c2 == 'G':
			return -1

def main():
	# read in the two strings
	f = open('/Volumes/Data/nick/Downloads/rosalind_tran.txt', 'r')
	lines = f.readlines()
	f.close()

	# a list with the two strings
	s = []
	for line in lines:
		if line[0] == '>':
			s.append('')
		else:
			s[-1] += line.split('\n')[0]

	s1 = s[0]
	s2 = s[1]

	transitions = 0
	transversions = 0
	# compare each character and count transversions and transitions
	for i in range(len(s[0])):
		res = compare(s1[i], s2[i])
		if res == 1:
			transitions += 1
		elif res == -1:
			transversions +=1

	print 'transitions = %d' % transitions
	print 'transversions = %d' % transversions

	print '%.11f' % (float(transitions) / transversions)

	return

	

if __name__ == '__main__':
	main()