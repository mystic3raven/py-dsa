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

# Accessing elements by index
colors = ("red", "green", "blue")
print(colors[0])  # Output: red
print(colors[1])  # Output: green

# Negative indexing
print(colors[-1])  # Output: blue

# concatenation 
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined = tuple1 + tuple2
print(combined)  # Output: (1, 2, 3, 4, 5, 6)

# repition 
numbers = (1, 2, 3)
repeated = numbers * 3
print(repeated)  # Output: (1, 2, 3, 1, 2, 3, 1, 2, 3)


#  slicing 
names = ("Alice", "Bob", "Charlie", "David")
subset = names[1:3]
print(subset)  # Output: ('Bob', 'Charlie')

# Slicing with step
every_other = names[::2]
print(every_other)  # Output: ('Alice', 'Charlie')

# tuplke methods

numbers = (1, 2, 3, 1, 1, 4)
print(numbers.count(1))  # Output: 3

# unpacking tuples
person = ("John", 30, "Engineer")
name, age, occupation = person
print(name)        # Output: John
print(age)         # Output: 30
print(occupation)  # Output: Engineer

# use cases 

# Using a tuple as a dictionary key
coordinates = {(0, 0): "Origin", (1, 2): "Point A", (2, 3): "Point B"}
print(coordinates[(1, 2)])  # Output: Point A

# Returning multiple values from a function
def get_position():
    return (10, 20)

x, y = get_position()
print(x, y)  # Output: 10 20
