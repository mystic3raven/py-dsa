# Creating a set with curly braces
fruits = {"apple", "banana", "cherry"}
print(fruits)  # Output: {'apple', 'banana', 'cherry'}

# Creating a set with the set() constructor
colors = set(["red", "green", "blue"])
print(colors)  # Output: {'red', 'green', 'blue'}

# Creating an empty set (note: {} creates an empty dictionary, not a set)
empty_set = set()
print(empty_set)  # Output: set()


# set operations 
numbers = {1, 2, 3}
numbers.add(4)
print(numbers)  # Output: {1, 2, 3, 4}


# removing elements
# remove() raises an error if the element does not exist
numbers.remove(2)
print(numbers)  # Output: {1, 3, 4}

# discard() does not raise an error if the element does not exist
numbers.discard(5)  # No error, even though 5 is not in the set

# pop() removes and returns an arbitrary element
popped_element = numbers.pop()
print(popped_element)  # Output: 1 (or any element, since the order is arbitrary)

# Union
set_a = {1, 2, 3}
set_b = {3, 4, 5}
union_set = set_a | set_b
print(union_set)  # Output: {1, 2, 3, 4, 5}

# intersections
set_a = {1, 2, 3}
set_b = {3, 4, 5}
union_set = set_a | set_b
print(union_set)  # Output: {1, 2, 3, 4, 5}


# difference
difference_set = set_a - set_b
print(difference_set)  # Output: {1, 2}


# symmetric difference
symmetric_difference_set = set_a ^ set_b
print(symmetric_difference_set)  # Output: {1, 2, 4, 5}

# add multiple elements
animals = {"cat", "dog"}
animals.add("rabbit")
print(animals)  # Output: {'cat', 'dog', 'rabbit'}

# discards
animals.discard("fish")  # No error, even though "fish" is not in the set

# pop
animals.discard("fish")  # No error, even though "fish" is not in the set

# union other sets
set_c = {5, 6, 7}
result = animals.union(set_c)
print(result)  # Output: {'cat', 'rabbit', 5, 6, 7}

# intersection
set_d = {"rabbit", 6, 8}
result = animals.intersection(set_d)
print(result)  # Output: {'rabbit'}

# difference
result = animals.difference(set_d)
print(result)  # Output: set() (since animals was cleared earlier)


# symmetric difference
result = set_c.symmetric_difference(set_d)
print(result)  # Output: {5, 7, 8}

# use cases 
if "apple" in fruits:
    print("Apple is in the set.")

# removing duplicates from a set
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = set(numbers)
print(unique_numbers)  # Output: {1, 2, 3, 4, 5}

