import networkx as nx
import openopt

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

# initialise a graph, where each node is a read
def init_graph(reads):
	G = nx.DiGraph()
	G.add_nodes_from(reads)

	return G

def compare_reads(r1,r2):
	"""Is there overlap between r1 and r2? Return length or r2 after overlap removed"""
	# overlap: r1 ... r2
	# starting position i in r1
	for i in range(len(r1)):
		looking_for = r1[i:]
		if (r2[:len(looking_for)] == looking_for):
			return len(looking_for)

	return 0

# create a directed edge between nodes that have overlap
def connect_reads(graph):
	for node in graph.nodes():
		other_nodes = graph.nodes()[:]
		other_nodes.remove(node)

		for other_node in other_nodes:
			overlap = compare_reads(node, other_node)
			if overlap >= len(other_node)/2:
				graph.add_edge(node, other_node, weight = overlap)

def main():
	# read the data from file
	reads = load_reads('/Volumes/Data/nick/Downloads/rosalind_long.txt')

	# create a graph, where each node is a read, and each directed edge is an overlap
	G = init_graph(reads)

	# connect the reads
	connect_reads(G)

	max_path = []
	for i in range(0, len(reads)):
		for j in range(0, len(reads)):
			if i != j:
				paths = nx.all_simple_paths(G, reads[i], reads[j])
				for path in paths:
					if len(path) == 50:
						max_path.append(path)

	superstring = ''
	for i in range(0, len(max_path[0])-1):
		overlap = compare_reads(max_path[0][i], max_path[0][i+1])
		# print overlap
		superstring = superstring + max_path[0][i][:-overlap]
	superstring += max_path[0][-1]

	print superstring

	return

if __name__ == '__main__':
	main()