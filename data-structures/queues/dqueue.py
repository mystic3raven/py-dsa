from collections import deque

# Example of Deque
d = deque()
d.append(1)        # Add to the right
d.appendleft(2)    # Add to the left
d.append(3)
d.appendleft(4)
print(d)           # Output: deque([4, 2, 1, 3])

d.pop()            # Remove from the right
print(d)           # Output: deque([4, 2, 1])

d.popleft()        # Remove from the left
print(d)           # Output: deque([2, 1])
