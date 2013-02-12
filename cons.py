import numpy

def main():
	    # load the file
    f = open('/Volumes/Data/nick/Downloads/rosalind_cons.txt', 'r')

    lines = f.readlines()

    strings = []
    for line in lines:
    	strings.append(line.split('\n')[0])

    # close the file
    f.close()

    # define m and n
    m = len(strings)
    n = len(strings[0])

    profile = numpy.zeros((4, n))
    idx = {0: 'A', 1: 'C', 2: 'G', 3: 'T'}

    # for each column
    for j in range(n):
    	# count each letter
    	for symbol in idx.keys():
    		# in each row
    		count = 0
    		for i in range(m):
    			if strings[i][j] == idx[symbol]:
    				count += 1
    		profile[symbol,j] = count

    consensus = profile.argmax(axis=0)
    consensus_letters = []
    for i in consensus:
    	consensus_letters.append(idx[i])

    # format the consensus strign for output
    consensus_output = ''.join(consensus_letters)
    print consensus_output

    # output the profile matrix
    for i in idx.keys():
    	s = '%s: ' % idx[i]
    	s += ' '.join(map(str,map(int,profile[i])))
    	print s

    return

if __name__ == '__main__':
	main()