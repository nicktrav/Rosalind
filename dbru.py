from operator import itemgetter, attrgetter


COMPLEMENTS = {'A':'T','C':'G','G':'C','T':'A'}
def rc(s):
	rev = s[::-1]
	rc = []

	for i in range(len(rev)):
		rc.append(COMPLEMENTS[rev[i]])

	return ''.join(rc)

def edges(S):
	o = []

	for r in S:
		o.append((r[:-1], r[1:]))

	return list(frozenset(o))

def main():
	# import and load the strings
	f = open('/Users/nick/Downloads/rosalind_dbru.txt', 'r')

	lines = f.read().split('\n')[:-1]

	f.close()

	S = frozenset(lines)
	Src = frozenset(map(rc, lines))

	B = list(S | Src)

	e = sorted(edges(B), key=itemgetter(0,1))

	for i in e:
		print '(%s, %s)' % (i[0], i[1])

if __name__ == '__main__':
	main()