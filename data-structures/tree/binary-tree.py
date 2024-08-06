class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

    def inorder_traversal(self, start, traversal):
        """Perform in-order traversal of the tree."""
        if start:
            traversal = self.inorder_traversal(start.left, traversal)
            traversal.append(start.data)
            traversal = self.inorder_traversal(start.right, traversal)
        return traversal

    def preorder_traversal(self, start, traversal):
        """Perform pre-order traversal of the tree."""
        if start:
            traversal.append(start.data)
            traversal = self.preorder_traversal(start.left, traversal)
            traversal = self.preorder_traversal(start.right, traversal)
        return traversal

    def postorder_traversal(self, start, traversal):
        """Perform post-order traversal of the tree."""
        if start:
            traversal = self.postorder_traversal(start.left, traversal)
            traversal = self.postorder_traversal(start.right, traversal)
            traversal.append(start.data)
        return traversal

# Usage
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

print("In-order Traversal:", tree.inorder_traversal(tree.root, []))  # Output: [4, 2, 5, 1, 3]
print("Pre-order Traversal:", tree.preorder_traversal(tree.root, []))  # Output: [1, 2, 4, 5, 3]
print("Post-order Traversal:", tree.postorder_traversal(tree.root, []))  # Output: [4, 5, 2, 3, 1]
