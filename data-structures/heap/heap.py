import heapq

# Create an empty heap
min_heap = []

# Add elements to the heap
heapq.heappush(min_heap, 10)
heapq.heappush(min_heap, 5)
heapq.heappush(min_heap, 15)
heapq.heappush(min_heap, 7)

# Get the smallest element
print("Smallest element:", heapq.heappop(min_heap))  # Output: 5

# Check the current state of the heap
print("Heap:", min_heap)  # Output: [7, 10, 15]
