import heapq

# Create an empty heap
min_heap = []

# Add elements to the heap
heapq.heappush(min_heap, 10)
heapq.heappush(min_heap, 5)
heapq.heappush(min_heap, 15)
heapq.heappush(min_heap, 7)

# Get the smallest element
smallest = heapq.heappop(min_heap)
print("Smallest element:", smallest)  # Output: 5

# Check the current state of the heap
print("Heap:", min_heap)  # Output: [7, 10, 15]

# Peek at the smallest element without removing it
smallest = min_heap[0]
print("Peek smallest element:", smallest)  # Output: 7

# Convert an unordered list into a heap
unordered_list = [3, 1, 4, 1, 5, 9, 2]
heapq.heapify(unordered_list)
print("Heapified list:", unordered_list)  # Output: [1, 1, 2, 3, 5, 9, 4]
