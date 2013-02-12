from math import factorial

def nCk(n , k):
	return factorial(n)/(factorial(k) * factorial(n - k))

def main():
	# open the text file
	f = open('/Volumes/Data/nick/Downloads/rosalind_iprb.txt', 'r')

	# read in the values
	[k, m, n] = map(int, f.readline().split('\n')[0].split(' '))

	# close the file
	f.close()	

	total_choices = float(4 * (nCk(k,2) + k*m + k*n + nCk(m,2) + m*n + nCk(n,2)))

	kk = nCk(k,2) * 4
	km = k * m * 4
	kn = k * n * 4
	mm =  nCk(m,2) * 3
	mn = m * n * 2

	print '%.5f' % ((kk + km + kn + mm + mn)/total_choices)

if __name__ == '__main__':
	main()