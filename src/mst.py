from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import minimum_spanning_tree, connected_components

class Graph():
	"""docstring for Graph"""
	def __init__(self, number_of_vertices):
		self.n = number_of_vertices+1
		# make a list of size NxN
		self.graph = [[0 for col in range(self.n)] for row in range(self.n) ]


	def addEdge(self, vertexA, vertexB, edge_weight):
		self.graph[vertexA][vertexB] = edge_weight
		self.graph[vertexB][vertexA] = edge_weight

		# we'll just update in serial order. Whoever wants a particular edge can have it there


	def getMSTWeight(self):

		X = csr_matrix(self.graph)

		n_components = connected_components(csgraph = X, directed = False, return_labels = False)

		if n_components <=2 :
			Tcsr = minimum_spanning_tree(X)
			return str(Tcsr.toarray().astype(int).sum())

		else:
			return -1


