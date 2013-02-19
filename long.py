import re

# load the reads in from file
def load_reads(f):
	f = open(f, 'r')

	lines = f.read().split('\n')[:-1]

	f.close()

	start_lines = []
	for i in range(len(lines)):
		if lines[i][0] == '>':
			start_lines.append(i)

	line_len = start_lines[1]

	s = []
	for start in start_lines:
		s.append(''.join(lines[start+1:start+line_len]))

	return s

# search for a read to splice to the end of the superstring.
# Return the read, the start position and length of the substring. Return Null if
# no candidate was found
def search_add_to_end(superstring, reads):
	# search for candidates to splice to END of superstring
	for start in range(0, len(superstring)):
		looking_for = superstring[start:]
		# print 'searching for \'%s\'' % looking_for
		for i in range(len(reads)):
			# print '\tin reads[%i] = %s' % (i, reads[i])
			end = len(looking_for)
			# print '\tend = %i' % -start
			# print '\t\treads[i][:end] = %s' % reads[i][:end+1]
			if reads[i][:end] == looking_for:
				# print '\t\tFOUND in read %d' % i
				# print '\t\twith end position %d' % end
				# print reads[i][-start:]				
				return (i, end, len(reads[i])-end)
	return (0,0,None)

# search for a read to splice to the START of the superstring.
# Return the read,the end position and length of substring. Return Null if
# no candidate was found
def search_add_to_start(superstring, reads):
	# search for candidates to splice to START of superstring
	for end in range(len(superstring), 0, -1):
		looking_for = superstring[:end]
		# print 'searching for \'%s\'' % looking_for
		for i in range(len(reads)):
			# print '\tin reads[%i] = %s' % (i, reads[i])
			start = len(reads[i]) - len(looking_for)
			# print '\tend = %i' % -start
			# print '\t\treads[i][:end] = %s' % reads[i][:end+1]
			if reads[i][start:] == looking_for:
				# print '\t\tFOUND in read %d' % i
				# print '\t\twith end position %d' % end
				# print reads[i][-start:]
				return (i, start, start)
	return (0,0,None)

# splice read[pos:] to end of superstring
# return the superstring
def splice_to_end(superstring, read, pos):
	return superstring + read[pos:]

# splice read[:pos] to start of superstring
# return the superstring
def splice_to_start(superstring, read, pos):
	# print read[:pos]
	return read[:pos+1] + superstring 

def main():
	# read the data from file
	reads = load_reads('/Volumes/Data/nick/Downloads/rosalind_long_1_dataset.txt')

	global full_len
	global half_len

	full_len = len(reads[0])

	# half the length of the reads
	if len(reads[0]) % 2 == 0:
		# even
		half_len = len(reads[0]) / 2
	else:
		# odd
		half_len = len(reads[0]) / 2 + 1

	# make the first read the start of the superstring
	superstring = reads[0]
	# remove from the list of reads
	reads.pop(0)

	# print search_add_to_end(superstring, reads)
	# return

	# print reads

	while reads != []:
		end_find = search_add_to_end(superstring, reads)
		start_find = search_add_to_start(superstring, reads)

		# print reads

		# superstring = splice_to_end(superstring, reads[end_find[0]], end_find[1])
		# reads.pop(end_find[0])

		# superstring = splice_to_start(superstring, reads[start_find[0]], start_find[1])
		# reads.pop(start_find[0])		

		# print end_find
		# print start_find

		if (end_find[2] < start_find[2]) and (end_find[2] != None):
			# print 'Splicing to END'
			superstring = splice_to_end(superstring, reads[end_find[0]], end_find[1])
			reads.pop(end_find[0])
		elif (start_find[2] < end_find[2]) and (start_find[2] != None):
			# print 'yes'
			# print 'Splicing to START'
			superstring = splice_to_start(superstring, reads[start_find[0]], start_find[1])
			reads.pop(start_find[0])
		else:
			# print 'Splicing to END'
			superstring = splice_to_end(superstring, reads[end_find[0]], end_find[1])
			reads.pop(end_find[0])
		# print superstring
		# print reads
		print len(reads)

	print superstring

	return	
	

if __name__ == '__main__':
	main()