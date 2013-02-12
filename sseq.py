
import re

def main():
	# get the strings s and t from file
	f = open('/Volumes/Data/nick/Downloads/rosalind_sseq.txt', 'r')

	[s, t] = f.read().split('\n')[0:-1]

	f.close()

	# convert t to a list of the t_i
	t = list(t)

	# the number of letters in t
	nt = len(t)

	# construct the regex
	itermediate_string = '.*?'
	pattern = itermediate_string
	for i in t:
		pattern += '(' + i + ')' + itermediate_string

	print 'Regex = \"%s\"' % pattern

	# run the regex
	prog = re.compile(pattern)
	res = prog.match(s)

	# get the indices
	indices = []
	for i in range(len(res.groups())):
		indices.append(res.start(i+1) + 1)

	print ' '.join(map(str,indices))

if __name__ == '__main__':
	main()