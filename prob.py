from math import log

def main():
	f = open('/Volumes/Data/nick/Downloads/rosalind_prob.txt', 'r')

	lines = f.readlines()

	f.close()

	s = list(lines[0].split('\n')[0])
	A = map(float, lines[1].split('\n')[0].split(' '))

	B = []

	
	for gc_content in A:
		prob = 0
		for i in s:
			if i == 'G' or i == 'C':
				prob += log(gc_content / 2, 10)
			else:
				prob += log((1 - gc_content) / 2, 10)

		B.append(prob)

	print ' '.join(map(str,B))

if __name__ == '__main__':
	main()