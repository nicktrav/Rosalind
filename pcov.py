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

def addNodes(G, l):
	"""Add elements of the list l as nodes to the graph, G"""
	G.add_nodes_from(l)

	return G

def addEdges(G, l, S):
	"""Add edges from the list l, to the graph G"""
	for kmer in l:
		prefix = kmer.prefix()
		suffix = kmer.suffix()

		if (prefix in G.nodes()) and (suffix in G.nodes()) and (kmer in S):
			G.add_edge(prefix, suffix, string=kmer)
		else:
			continue

def main():

	# open the file of strings
	with open('/Users/nick/Downloads/rosalind_pcov.txt', 'r') as f:
		lines = f.read().split('\n')[:-1]

	# instantiate the DNAStrings
	S = []
	Src = []
	for s in lines:
		S.append(DNAString(s))
		Src.append(DNAString(s).reverseComplement())

	SuSrc = list(set(S).union(Src))

	prefixSuffix = []
	for i in SuSrc:
		prefixSuffix.append(i.prefix())
		prefixSuffix.append(i.suffix())

	prefixSuffix = list(set(prefixSuffix))

	# instantiate the graph
	G = nx.DiGraph()

	# add nodes
	addNodes(G, prefixSuffix)

	# add edges
	addEdges(G, SuSrc, S)

	# the simple cycles of the graph
	cycles = list(nx.simple_cycles(G))

	# if there is more than one simple cycle, raise error
	if len(cycles) > 1:
		print 'More than one simple cycle!?'
		print cycles
	else:
		print ''.join(map(lambda x: x[-1], cycles[0]))


if __name__ == '__main__':
	main()