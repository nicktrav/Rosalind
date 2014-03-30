f = {0: 0, 1: 1}

def fibbo(n):

	if n in f:
		return f[n]
	else:
		f[n] = fibbo(n-1) + fibbo(n-2)
		return fibbo(n)

def main():
	print fibbo(1)

if __name__ == '__main__':
	main()