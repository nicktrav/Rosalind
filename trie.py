import networkx as nx
import matplotlib.pyplot as plt
import pydot
import graphviz

COUNTER = 1

def items_with_first(l, f):
	o = []

	for i in l:
		if i[0] == f: o.append(i)

	return o

def remove_first_letter(s):
	if len(s) != 0:
		return s[1:]
	else:
		return None

def get_branching_letters(l):
	s = []
	for i in l:
		if i[0] not in s:
			s.append(i[0])

	return s

def branch(G, pointer):
	global COUNTER

	# print 'Currently here: %s' % G.node[pointer]
	if G.node[pointer]['items'] == None:
		# 'Nothing to do here ... leaving'
		return

	# get the first letters
	to_branch = get_branching_letters(G.node[pointer]['items'])
	# print 'Branching letters are ' + str(to_branch)
	# print to_branch
	for b in to_branch:
		# print 'COUNTER = %d' % COUNTER
		COUNTER += 1
		# get a list of the items to add to the next node
		items_to_add = map(remove_first_letter,items_with_first(G.node[pointer]['items'], b))
		if items_to_add == ['']: items_to_add = None
		# print '\tCreating node with items: %s' % items_to_add
		# add the new node, with the items
		G.add_node(COUNTER, items=items_to_add, name=COUNTER)
		# print '\tCreated new node %d' % COUNTER
		# add a link from the current node to the node just added
		G.add_edge(pointer, COUNTER, label=b)
		# print '\tCreated edge (%d, %d)' % (pointer, COUNTER)

	# print 'Edges from here %s' % str(G.edges(pointer))
	for edge in G.edges(pointer):
		# print '\tFollowing edge: %s, to branch on node with items %s' % (str(edge), str(G.node[edge[pointer]]['items']))
		if edge[1] < pointer: continue
		branch(G, edge[1])

	return

def main():
	# load data
	f = open('/Users/nick/Downloads/rosalind_trie.txt', 'r')

	lines = f.read().split('\n')[:-1]

	f.close()

	# create the graph
	G = nx.Graph()

	# create the root node (i.e. initialise the graph)
	G.add_node(COUNTER, items=lines, name=COUNTER)
	pointer = COUNTER
	
	branch(G, pointer)

	# print the output
	for edge in G.edges():
		print '%d %d %s' % (edge[0], edge[1], G.edge[edge[0]][edge[1]]['label'])

	# pos=nx.graphviz_layout(G,prog='dot')
	# nx.draw(G,pos,arrows=False)
	# plt.show()

if __name__ == '__main__':
	main()