class FenwickTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (size + 1)  # Tree is 1-indexed

    def update(self, index, delta):
        """Add delta to the element at index."""
        while index <= self.size:
            self.tree[index] += delta
            index += index & -index
        print(f"Updated tree: {self.tree}")

    def prefix_sum(self, index):
        """Compute the prefix sum from start to index."""
        result = 0
        while index > 0:
            result += self.tree[index]
            index -= index & -index
        return result

    def range_sum(self, left, right):
        """Compute the range sum from left to right."""
        return self.prefix_sum(right) - self.prefix_sum(left - 1)

# Usage
data = [1, 3, 5, 7, 9, 11]
fenwick_tree = FenwickTree(len(data))

# Build the tree by updating it with initial values
for i, value in enumerate(data, start=1):
    fenwick_tree.update(i, value)

# Query the sum from index 1 to 3 (1-based index)
print("Sum of range [1, 3]:", fenwick_tree.range_sum(1, 3))  # Output: 9 (1 + 3 + 5)

# Update index 2 (1-based) by adding 5
fenwick_tree.update(2, 5)

# Query the sum from index 1 to 3 again
print("Sum of range [1, 3] after update:", fenwick_tree.range_sum(1, 3))  # Output: 14 (1 + 8 + 5)
