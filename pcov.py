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

def main():
	# open the file of strings
	with open('/Users/nick/Downloads/rosalind_pcov.txt', 'r') as f:
		lines = f.read().split('\n')

	# instantiate the DNAStrings
	S = []
	for s in lines:
		S.append(DNAString(s))

	# the reverse complement
	Src = S
	for s in Src:
		s.reverseComplement()

	both = list(set(S) | set(Src))
	print both
	 
	o = []
	for i in both:
		o.append(i.prefix())
		o.append(i.suffix())

	print list(set(o))


if __name__ == '__main__':
	main()