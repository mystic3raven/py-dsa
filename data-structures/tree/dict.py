# Creating a dictionary with curly braces
person = {"name": "Alice", "age": 30, "city": "New York"}
print(person)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York'}

# Creating a dictionary with the dict() constructor
car = dict(make="Toyota", model="Corolla", year=2020)
print(car)  # Output: {'make': 'Toyota', 'model': 'Corolla', 'year': 2020}

# Creating an empty dictionary
empty_dict = {}
print(empty_dict)  # Output: {}

# Accessing dictionary values
# Creating a dictionary with curly braces
person = {"name": "Alice", "age": 30, "city": "New York"}
print(person)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York'}

# Creating a dictionary with the dict() constructor
car = dict(make="Toyota", model="Corolla", year=2020)
print(car)  # Output: {'make': 'Toyota', 'model': 'Corolla', 'year': 2020}

# Creating an empty dictionary
empty_dict = {}
print(empty_dict)  # Output: {}

# Modifying dictionary values
# Adding a new key-value pair
person["email"] = "alice@example.com"
print(person)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York', 'email': 'alice@example.com'}

# Updating an existing key-value pair
person["age"] = 31
print(person)  # Output: {'name': 'Alice', 'age': 31, 'city': 'New York', 'email': 'alice@example.com'}

# Removing a key-value pair
# Using del to remove a key-value pair
del person["email"]
print(person)  # Output: {'name': 'Alice', 'age': 31, 'city': 'New York'}

# Using pop() to remove a key-value pair and return its value
age = person.pop("age")
print(age)     # Output: 31
print(person)  # Output: {'name': 'Alice', 'city': 'New York'}

# Using popitem() to remove and return an arbitrary key-value pair (from Python 3.7, it's the last inserted pair)
item = person.popitem()
print(item)    # Output: ('city', 'New York')
print(person)  # Output: {'name': 'Alice'}

# Dictionary methods

keys = person.keys()
print(keys)  # Output: dict_keys(['name'])

values = car.values()
print(values)  # Output: dict_values(['Toyota', 'Corolla', 2020])

items = car.items()
print(items)  # Output: dict_items([('make', 'Toyota'), ('model', 'Corolla'), ('year', 2020)])

person.update({"age": 32, "country": "USA"})
print(person)  # Output: {'name': 'Alice', 'age': 32, 'country': 'USA'}

car.clear()
print(car)  # Output: {}

# Dictionary comprehension
# Creating a dictionary with squares of numbers
squares = {x: x*x for x in range(1, 6)}
print(squares)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Creating a dictionary by transforming another dictionary
names = {"Alice": 25, "Bob": 30, "Charlie": 35}
uppercase_names = {k.upper(): v for k, v in names.items()}
print(uppercase_names)  # Output: {'ALICE': 25, 'BOB': 30, 'CHARLIE': 35}

# Using case for Dcitionary

# Mapping names to phone numbers
phone_book = {"Alice": "123-4567", "Bob": "987-6543"}
print(phone_book["Alice"])  # Output: 123-4567

# Counting the frequency of characters in a string
text = "hello world"
frequency = {}
for char in text:
    frequency[char] = frequency.get(char, 0) + 1
print(frequency)  # Output: {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}

# Caching and Memoization
cache = {}
def fib(n):
    if n in cache:
        return cache[n]
    if n <= 1:
        return n
    cache[n] = fib(n-1) + fib(n-2)
    return cache[n]

print(fib(10))  # Output: 55

