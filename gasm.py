import networkx as nx

class DNAString(object):
	"""DNA String class"""
	def __init__(self, string):
		self.string = string

	def __str__(self):
		return self.string

	def __eq__(self, other):
		return self.string == other.string

	# define the hash for the set function
	def __hash__(self):
		return hash(self.string)

	def __repr__(self):
		return self.string

	def reverse(self):
		"""The reverse of the string"""
		self.string = self.string[::-1]
		return self

	def complement(self):
		"""The complement of the string S"""
		o = []
		for i in self.string:
			if i == 'A': o.append('T')
			if i == 'C': o.append('G')
			if i == 'G': o.append('C')
			if i == 'T': o.append('A')

		self.string = ''.join(o)
		return self

	def reverseComplement(self):
		"""The reverse complement of the string S"""
		self.reverse()
		self.complement()
		return self

	def prefix(self):
		return self.string[:-1]

	def suffix(self):
		return self.string[1:]

	def kmers(self, k):
		return [DNAString(self.string[i:i+k]) for i in range(len(self.string) - k + 1)]


def addNodes(G, l):
	"""Add elements of the list l as nodes to the graph, G"""
	G.add_nodes_from(l)

	return G

def addEdges(G, l):
	"""Add edges from the list l, to the graph G"""
	for kmer in l:
		prefix = kmer.prefix()
		suffix = kmer.suffix()

		# if (prefix in G.nodes()) and (suffix in G.nodes()) and (kmer in S):
		if (prefix in G.nodes()) and (suffix in G.nodes()):
			G.add_edge(prefix, suffix, string=kmer)
		else:
			continue

def cycles_k(S, k):
	"""Look for cycles in the set of all k-mers o"""

	S_kmers = []
	S_rc_kmers = []

	for s in S:
		S_kmers.extend(s.kmers(k))
		S_rc_kmers.extend(DNAString(s.string).reverseComplement().kmers(k))

	# remove duplicates
	S_kmers = list(set(S_kmers))
	S_rc_kmers = list(set(S_rc_kmers))

	# the union of S and Src of kmers
	SuSrc_kmers = list(set(S_kmers) | set(S_rc_kmers))

	prefixSuffix = []
	for i in SuSrc_kmers:
		prefixSuffix.append(i.prefix())
		prefixSuffix.append(i.suffix())

	prefixSuffix = list(set(prefixSuffix))

	# initialise the directed graph
	G = nx.DiGraph()

	# add nodes
	addNodes(G, prefixSuffix)

	# add edges
	addEdges(G, SuSrc_kmers)

	# the simple cycles of the graph
	cycles = list(nx.simple_cycles(G))

	# return the cycles
	return cycles

def formCyclicStrings(cycles):
	"""Form the cyclic strings by join the last base-pair
	from each node in the cycle."""
	cyclicStrings = []

	for cycle in cycles:
		cyclicStrings.append( ''.join(map(lambda s: s[-1], cycle)) )

	return cyclicStrings

def main():

	# open the file of strings
	with open('/Users/nick/Downloads/rosalind_gasm.txt', 'r') as f:
		lines = f.read().split('\n')[:-1]

	# instantiate the DNAStrings
	S = []
	for s in lines:
		S.append(DNAString(s))
	
	# work backwards from the k = len(s)
	for k in range(len(S[0].string), 0, -1):
		# look for cycles
		cycles = cycles_k(S, k)

		# when we have found the case where there
		# are two cycles, we are done
		if len(cycles) == 2:
			cyclicStrings = formCyclicStrings(cycles)
			print 'Found @ k = %d' % k
			break

	# return one of the cyclic strings
	print cyclicStrings[0]

	return

if __name__ == '__main__':
	main()