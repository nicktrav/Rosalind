import itertools, random

def main():
	# open the file
	f = open('/Volumes/Data/nick/Downloads/rosalind_perm.txt', 'r');

	# close the file
	f.close()

	a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	b = [3, 1, 5, 2, 7, 4, 9, 6, 10, 8]

	# compute all possible reversals
	intervals = []
	for size in range(1,11):
		number_of_intervals = 11-size
		start = 0
		end = start + size
		for i in range(1,number_of_intervals + 1):
			intervals.append([start, end])
			start += 1
			end += 1

	number_of_intervals = len(intervals)

	same = 0
	counter = 0
	random.seed()

	for i in range(100):
		# choose a random interval
		interval = intervals[random.randrange(number_of_intervals)]

		# reverse this interval
		b[interval[0]:interval[1]] = reversed(b[interval[0]:interval[1]])
		print 'b = %s' % b

		if a == b:
			same = 1
			print 'THEY ARE THE SAME!'

		# increment the counter
		counter += 1

if __name__ == '__main__':
	main()