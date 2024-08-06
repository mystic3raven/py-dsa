# Custom min-heap implementation

class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    def insert(self, key):
        """Insert a new key into the heap."""
        self.heap.append(key)
        i = len(self.heap) - 1

        # Fix the min-heap property if it is violated
        while i != 0 and self.heap[self.parent(i)] > self.heap[i]:
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)

    def heapify(self, i):
        """Ensure the heap property is maintained starting from index i."""
        smallest = i
        left = self.left_child(i)
        right = self.right_child(i)

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left

        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.heapify(smallest)

    def extract_min(self):
        """Remove and return the smallest element from the heap."""
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify(0)

        return root

    def peek(self):
        """Return the smallest element without removing it."""
        if len(self.heap) == 0:
            return None
        return self.heap[0]

# Usage
min_heap = MinHeap()
min_heap.insert(10)
min_heap.insert(5)
min_heap.insert(15)
min_heap.insert(7)

print("Extracted Min:", min_heap.extract_min())  # Output: 5
print("Current Min:", min_heap.peek())           # Output: 7
