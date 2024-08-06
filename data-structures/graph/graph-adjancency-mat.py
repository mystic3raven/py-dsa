# Graph by Adjacency Matrix

class Graph:
    def __init__(self, num_vertices):
        self.adj_matrix = [[0] * num_vertices for _ in range(num_vertices)]
        self.num_vertices = num_vertices

    def add_edge(self, vertex1, vertex2):
        if 0 <= vertex1 < self.num_vertices and 0 <= vertex2 < self.num_vertices:
            self.adj_matrix[vertex1][vertex2] = 1
            self.adj_matrix[vertex2][vertex1] = 1  # For undirected graph
            print(f"Added edge between {vertex1} and {vertex2}.")

    def display(self):
        for row in self.adj_matrix:
            print(row)

# Usage
g = Graph(3)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.display()
# Output:
# [0, 1, 1]
# [1, 0, 1]
# [1, 1, 0]
