import re

# Find all substrings of length l in string s
def generate_substrings(s, l):
	# make sure s < l
	if l > len(s):
		print 'Cannot have l > len(s)!'
		return -1

	substrings = []

	index_end = l
	index_start = 0
	while index_end <= len(s):
		trial = s[index_start:index_end]
		if trial not in substrings:
			substrings.append(s[index_start:index_end])
		index_end += 1
		index_start += 1

	return substrings

def main():
	# open the file
	# f = open('test.txt', 'r')
	f = open('/Volumes/Data/nick/Downloads/rosalind_lcs.txt', 'r')

	# create a list of the strings
	# strings = f.read().split('\n')

	lines = f.readlines()
	strings = []
	for line in lines:
		strings.append(line.split('\n')[0])

	# close the file
	f.close()

	# find the string with the minimum length to generate the substrings
	min_string = sorted(strings, key=len)[0]
	# remove the minimum string
	strings.remove(min_string)

	# a list of the common substrings (i.e. substring occurs in ALL the strings)
	common_subs = []

	# starting with the whole minimum string
	# for i in range(len(min_string), 900, -1):
	# for i in range(1, len(min_string), 1):
	for i in range(100, 130, 1):
		# print 'Searching at level i = %i' % i
		found_at_level = 0
		# generate the possible substrings of length i
		substrings = generate_substrings(min_string, i)
		# for each of the generate substrings
		for substring in substrings:
			# set the found counter to zero
			found_counter = 0
			# search for the substring in the remaining strings
			for s in strings:
				match = re.search(substring, s)
				if match:
					# print 'Found substring "%s" in string "%s" at position %i' % (substring, s, match.start())
					found_counter = found_counter + 1
					if found_counter == len(strings):
						# print '%s found in all strings! i = %i' % (substring, i)
						common_subs = substring
						found_at_level += 1

			# if substrings.index(substring) == len(substrings) and found_counter == 0:
			# 	print common_subs
			# 	return

		print 'Found %i common substrings at level %i' % (found_at_level, i)
		if found_at_level == 0:
			print common_subs
			return

	print common_subs
	return


if __name__ == '__main__':
	main()