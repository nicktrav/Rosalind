import itertools, random

# generate a random permuation
def random_permutation(iterable, r=None):
    "Random selection from itertools.permutations(iterable, r)"
    pool = tuple(iterable)
    r = len(pool) if r is None else r
    return list(random.sample(pool, r))

def numbers_greater(l):
	l_greater = []

	for i in range(len(l)):
		count_greater = 0

		for j in range(i+1, len(l)):
			if l[j] > l[i]:
				count_greater += 1

		l_greater.append(count_greater)

	return l_greater

def numbers_lower(l):
	l_lower = []

	for i in range(len(l)):
		count_lower = 0

		for j in range(i+1, len(l)):
			if l[j] < l[i]:
				count_lower += 1

		l_lower.append(count_lower)

	return l_lower

# a function that removes items in a list, 'l' that are LESS THAN
# the first element, 'i'
def remove_unviable_inc(l):
	temp = l[:]

	for i in sorted(temp, reverse=True):
		if i < l[0]:
			temp.remove(i)

	# for i in range(1, l[0]):
	# 	if i in temp: temp.remove(i)

	return temp

# a function that removes items in a list, 'l' that are GREATER THAN
# the first element, 'i'
def remove_unviable_dec(l):
	temp = l[:]

	for i in sorted(temp, reverse=True):
		if i > l[0]:
			temp.remove(i)

	# for i in range(l[0]+1, max(l)+1):
	# 	if i in temp: temp.remove(i)

	return temp

def find_first_max(l):
	return l.index(max(l))

# generate the largest increasing subsequence
def largest_increasing(pi):
	# a copy of pi
	l = pi[:]
	# the list to return
	subsequence = []

	while l != []:
		# print l
		# generate the numbers_greater list
		l_numbers_greater = numbers_greater(l)
		# print l_numbers_greater
		# get the index of the item to add to the list
		idx_to_add = l_numbers_greater.index(max(l_numbers_greater))
		# print idx_to_add
		# remove items to the left of this index
		l = l[idx_to_add:]
		# print l
		# remove items that are less than this value
		l = remove_unviable_inc(l)
		# add the item to the subsequence list
		subsequence.append(l.pop(0))
		# print subsequence

	return subsequence

# generate the largest increasing subsequence
def largest_decreasing(pi):
	# a copy of pi
	l = pi[:]
	# the list to return
	subsequence = []

	while l != []:
		# print 'l = \t\t\t\t%s' % l
		# generate the numbers_lower list
		l_numbers_lower = numbers_lower(l)
		# print 'l_numbers_lower = \t%s' % l_numbers_lower
		# get the index of the item to add to the list
		idx_to_add = l_numbers_lower.index(max(l_numbers_lower))
		# print 'idx_to_add = %s' % idx_to_add
		# remove items to the left of this index
		l = l[idx_to_add:]
		# print 'l after removal = \t%s' % l
		# remove items that are greater than this value
		l = remove_unviable_dec(l)
		# print 'l after removal 2 = %s' % l
		# add the item to the subsequence list
		subsequence.append(l.pop(0))
		# print subsequence

	return subsequence

def test_output(fl):
	f = open(fl, 'r')

	lines = f.read().split('\r\n')

	a = map(int, lines[0].split(' '))
	b = map(int, lines[1].split(' '))

	f.close()

	print a
	print b

	for i in range(len(a)-1):
		if a[i] > a[i+1]:
			print 'ERROR FOUND! -- %i > %i' % (a[i], a[i+1])

	for i in range(len(b)-1):
		if b[i] < b[i+1]:
			print 'ERROR FOUND! -- %i < %i' % (b[i], b[i+1])		

	return

def main():
	# import file
	f = open('/Volumes/Data/nick/Downloads/rosalind_lgis.txt', 'r')

	lines = f.read().split('\n')

	f.close()

	n = int(lines[0])
	pi = map(int, lines[1].split(' '))

	pi = random_permutation(range(1,6))
	# pi = [8, 2, 1, 6, 5, 7, 4, 3, 9]

	# print pi

	# print numbers_greater(pi)

	# print ' '.join(map(str, largest_increasing(pi)))
	# print ' '.join(map(str, largest_decreasing(pi)))

	# test_output('/Volumes/Data/nick/Downloads/rosalind_lgis_2_output.txt')

if __name__ == '__main__':
	main()