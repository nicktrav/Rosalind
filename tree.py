import networkx as nx

def create_tree(n, arcs):
	# create the graph
	G = nx.Graph()

	# add the nodes
	G.add_nodes_from(range(1, n+1))

	# add the arcs
	G.add_edges_from(arcs)
	
	return G

def main():
	# read contents from file
	f = open('/Volumes/Data/nick/Downloads/rosalind_tree.txt', 'r')

	lines = f.read().split('\n')

	f.close()

	# define the number of nodes, 'n'
	n = int(lines[0])
	# print n

	# define the list of arcs
	arcs = []
	[arcs.append(tuple(map(int, arc.split(' ')))) for arc in lines[1:]]
	# print arcs

	# create the tree
	tree = create_tree(n, arcs)

	# do a flood fill
	# source: http://en.wikipedia.org/wiki/Flood_fill

	return

if __name__ == '__main__':
	main()