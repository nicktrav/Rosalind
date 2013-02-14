import networkx as nx
from operator import itemgetter, attrgetter

def create_tree(n, arcs):
	# create the graph
	G = nx.Graph()

	# add the nodes
	G.add_nodes_from(range(1, n+1))

	# add the arcs
	G.add_edges_from(arcs)
	
	return G

# a fundtion to find the disconnected groups of the graph.
# Returns the node from each group with the largest degree.
# Uses a flood fill to find the groups
def find_disconnected_groups(graph):
	
	# create a dictionary of the nodes of the graph with their colour
	node_colours = {}
	for i in graph.nodes():
		node_colours[i] = None

	colour_counter = 0
	groups = {}

	# while all the nodes are uncoloured
	while (None in node_colours.values()):
		for i in graph.nodes():
			# if it is uncoloured, colour it and find
			# all of the nodes connected to it and colour them
			if node_colours[i] == None:
				node_colours[i] = colour_counter
				groups[colour_counter] = [i]
				for j in graph.nodes():
					if nx.has_path(graph, i, j) == True:
						node_colours[j] = node_colours[i]
						if j not in groups[colour_counter]:
							groups[colour_counter].append(j)
				colour_counter += 1
				# print node_colours

	# the number of groups
	n_groups = max(groups.keys()) + 1

	return groups

# given a graph and its ditinct groups,
# return the node from each group with the
# highest degree
def max_degree(graph, groups):
	nodes = []

	# find the max node from each group
	for group in groups.values():
		max_degree = 0
		max_node = group[0]
		for node in group:
			if graph.degree(node) > max_degree:
				max_node = node
				max_degree = graph.degree(node)
		nodes.append((max_node, max_degree))

	return nodes

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
	[arcs.append(tuple(map(int, arc.split(' ')))) for arc in lines[1:-1]]
	# print arcs

	# create the graph
	G = create_tree(n, arcs)

	# find the disconnected groups
	# source: http://en.wikipedia.org/wiki/Flood_fill
	groups = find_disconnected_groups(G)

	# output the number of arcs needed to form a tree
	print len(groups) - 1

	# find the highest degree node for each group
	max_degrees = max_degree(G, groups)
	
	# output the maximum degree node per group, with degree
	print sorted(max_degrees, key=itemgetter(1), reverse=True)


	return

if __name__ == '__main__':
	main()