import abc
import numpy as np


class Graph(abc.ABC):

    def __init__(self, numVertices, directed=False):

        # vertices_id ranges from 0 to numVertices - 1
        self.numVertices = numVertices
        self.directed = directed

# build up graphs by addding edges that connect to two vertices together
    @abc.abstractmethod
    def add_edge(self, v1, v2, weight):
        pass

    @abc.abstractmethod
    def get_adjacent_vertices(self, v):
        pass

    @abc.abstractmethod
    # retrieve number of edges incident/flow into a vertix
    def get_indegree(self, v):
        pass

    @abc.abstractmethod
    # given to vertices,it gets the weight
    def get_edge_weight(self, v1, v2):
        pass

    @abc.abstractmethod
    def display(self):
        pass

###############################################################
# Represents a graph as an adjacent matrix.A cell in the Matrix
# has a value where there exist and edge between the vertex represented by the row and column numbers.

# Weighted graphs can hold values > 1 in the matrix cells,
#  value of Zero indcicates that there is no edge


class AdjacencyMatrixGraph(Graph):

    def __init__(self, numVertices, directed=False):
        super(AdjacencyMatrixGraph, self).__init__(numVertices, directed)

        self.matrix = np.zeros((numVertices, numVertices))

    def add_edge(self, v1, v2, weight=1):
        if v1 >= self.numVertices or v2 >= self.numVertices or v1 < 0 or v2 < 0:
            raise ValueError("Vertices %d and %d are out of bounds" % (v1, v2))

        if weight < 1:
            raise ValueError("An edge cannot have weight less than 1")

        # entry in a cell is equal to the weight of that cell.
        self.matrix[v1, v2] = weight

        if self.directed == False:
            self.matrix[v2][v1] = weight

    def get_adjacent_vertices(self, v):
        if v < 0 or v >= self.numVertices:
            raise ValueError("Cannot access vertex %d" % v)

        adjacent_vertices = []
        for i in range(self.numVertices):
            if self.matrix[v][i] > 0:
                adjacent_vertices.append(i)

        return adjacent_vertices

    def get_indegree(self, v):
        if v < 0 or v >= self.numVertices:
            raise ValueError("cannot access vertex %d" % v)

        indegree = 0
        for i in range(self.numVertices):
            if self.matrix[i][v] > 0:
                indegree = indegree + 1
        return indegree

    def get_edge_weight(self, v1, v2):
        return self.matrix[v1][v2]

    def display(self):
        for i in range(self.numVertices):
            for v in self.get_adjacent_vertices(i):
                print(i, "---->", v)


g = AdjacencyMatrixGraph(4)

g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(2, 3)

for i in range(4):
    print("Adjacent to: ", i,  g.get_adjacent_vertices(i))

for i in range(4):
    print("Indgegree: ", i,  g.get_indegree(i))

for i in range(4):
    for j in g.get_adjacent_vertices(i):
        print("Edge weigth: ", i, "", j, "Weight: ", g.get_edge_weight(i, j))
g.display()
