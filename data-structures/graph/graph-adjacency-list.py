# #
# Graphs can be represented in various ways, including adjacency matrices and adjacency lists.
# 1. Adjacency List

# An adjacency list represents a graph as a collection of lists. Each vertex has a list of adjacent vertices. 
# This representation is space-efficient for sparse graphs.

class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []
            print(f"Added vertex {vertex}.")

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.graph and vertex2 in self.graph:
            self.graph[vertex1].append(vertex2)
            self.graph[vertex2].append(vertex1)  # For undirected graph
            print(f"Added edge between {vertex1} and {vertex2}.")

    def display(self):
        for vertex, edges in self.graph.items():
            print(f"{vertex}: {edges}")

# Usage
g = Graph()
g.add_vertex(0)
g.add_vertex(1)
g.add_vertex(2)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.display()
# Output:
# 0: [1, 2]
# 1: [0, 2]
# 2: [0, 1]
