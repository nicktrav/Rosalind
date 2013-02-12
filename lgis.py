import itertools

# a function to generate a subsequence of length i from a list of length n
def generate_removal_indices(i, n):
	removal_indices = []
	for i in itertools.combinations(range(n), i):
		removal_indices.append(list(i))

	return removal_indices

# remove from list 'l', items 'r'
def remove_items(l, r):
	temp = l[:]

	for item in sorted(r, reverse=True):
		temp.pop(item)

	return temp

# generate a list of lists corresponding to the original
# list 'l' with each set of indices 's' removed
def removed_list(l, s):
	new_lists = []

	for i in s:
		new_lists.append(remove_items(l[:], i))

	return new_lists

# a function to test if a subsequence is increasing
def is_increasing(subsequence):
	for i in range(len(subsequence)-1):
		if subsequence[i+1] < subsequence[i]:
			return -1

	return 1

# a function to test if a subsequence is decreasing
def is_decreasing(subsequence):
	for i in range(len(subsequence)-1):
		if subsequence[i+1] > subsequence[i]:
			return -1

	return 1	

# a function to find the longest increasing subsequence
def longest_increasing(n, pi):
	longest = []

	for i in range(1, n):
		# generate a list with 'i' enements removed
		indices = generate_removal_indices(i, n)
		subsequences = removed_list(pi, indices)

		# test if the subsequence is increasing
		for subsequence in subsequences:
			if is_increasing(subsequence) == 1:
				return subsequence

	return longest

def main():
	# import file
	f = open('/Volumes/Data/nick/Downloads/rosalind_lgis.txt', 'r')

	lines = f.read().split('\n')

	f.close()

	# define the variables 'n' and 'pi'
	n = int(lines[0])
	pi = map(int, lines[1].split(' '))

	print longest_increasing(n, pi)
	# print removed_list(pi, [[0], [0,1]])
	# longest_increasing(n, pi)

if __name__ == '__main__':
	main()