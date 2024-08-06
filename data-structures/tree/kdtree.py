class KDNode:
    def __init__(self, point, left=None, right=None):
        self.point = point
        self.left = left
        self.right = right

class KDTree:
    def __init__(self, points):
        self.k = len(points[0])  # Dimension of the points
        self.root = self.build(points, depth=0)

    def build(self, points, depth):
        if not points:
            return None

        # Select axis based on depth so that axis cycles through all valid values
        axis = depth % self.k

        # Sort point list and choose median as pivot element
        points.sort(key=lambda x: x[axis])
        median = len(points) // 2

        # Create node and construct subtrees
        return KDNode(
            point=points[median],
            left=self.build(points[:median], depth + 1),
            right=self.build(points[median + 1:], depth + 1)
        )

    def nearest_neighbor(self, point, return_distance=False):
        """Find the nearest neighbor to the given point."""
        def nn_search(node, depth):
            if node is None:
                return None, float('inf')

            axis = depth % self.k
            next_branch = None
            opposite_branch = None

            # Choose the side to explore
            if point[axis] < node.point[axis]:
                next_branch = node.left
                opposite_branch = node.right
            else:
                next_branch = node.right
                opposite_branch = node.left

            # Recursively search the nearest neighbor
            best, best_dist = nn_search(next_branch, depth + 1)

            # Check the distance of the current node
            current_dist = self.distance(point, node.point)
            if current_dist < best_dist:
                best = node.point
                best_dist = current_dist

            # Check if we need to explore the opposite branch
            if abs(point[axis] - node.point[axis]) < best_dist:
                potential_best, potential_dist = nn_search(opposite_branch, depth + 1)
                if potential_dist < best_dist:
                    best = potential_best
                    best_dist = potential_dist

            return best, best_dist

        nearest, distance = nn_search(self.root, 0)
        return (nearest, distance) if return_distance else nearest

    @staticmethod
    def distance(point1, point2):
        """Compute the Euclidean distance between two points."""
        return sum((x - y) ** 2 for x, y in zip(point1, point2)) ** 0.5

# Usage
points = [(2, 3), (5, 4), (9, 6), (4, 7), (8, 1), (7, 2)]
kd_tree = KDTree(points)

target = (9, 2)
nearest = kd_tree.nearest_neighbor(target)
print(f"Nearest neighbor to {target} is {nearest}")
