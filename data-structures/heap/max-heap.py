# max heap implementation

import heapq

# Create an empty max-heap
max_heap = []

# Add elements to the max-heap
heapq.heappush(max_heap, -10)
heapq.heappush(max_heap, -5)
heapq.heappush(max_heap, -15)
heapq.heappush(max_heap, -7)

# Get the largest element
largest = -heapq.heappop(max_heap)
print("Largest element:", largest)  # Output: 15

# Check the current state of the max-heap
print("Max-Heap:", [-x for x in max_heap])  # Output: [10, 7, 5]

# Peek at the largest element without removing it
largest = -max_heap[0]
print("Peek largest element:", largest)  # Output: 10

# Convert an unordered list into a max-heap
unordered_list = [3, 1, 4, 1, 5, 9, 2]
max_heap = [-x for x in unordered_list]
heapq.heapify(max_heap)
print("Max-Heapified list:", [-x for x in max_heap])  # Output: [9, 5, 4, 1, 1, 3, 2]
