class DisjointSet:
    def __init__(self, n):
        # Initialize n disjoint sets with each element being its own parent
        self.parent = list(range(n))
        # Initialize ranks to 0
        self.rank = [0] * n

    def find(self, x):
        """Find the representative of the set containing x with path compression."""
        if self.parent[x] != x:
            # Recursively find the root and compress the path
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        """Union the sets containing x and y."""
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            # Union by rank
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1

            print(f"Union: ({x}, {y}) - New parents: {self.parent}")

# Usage
n = 5  # Number of elements
disjoint_set = DisjointSet(n)

# Union operations
disjoint_set.union(0, 1)
disjoint_set.union(1, 2)
disjoint_set.union(3, 4)

# Find operations
print("Find(0):", disjoint_set.find(0))  # Output: Representative of the set containing 0
print("Find(3):", disjoint_set.find(3))  # Output: Representative of the set containing 3

# Checking connectivity
print("Are 0 and 2 connected?", disjoint_set.find(0) == disjoint_set.find(2))  # Output: True
print("Are 0 and 4 connected?", disjoint_set.find(0) == disjoint_set.find(4))  # Output: False
