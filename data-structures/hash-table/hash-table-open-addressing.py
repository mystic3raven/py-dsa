# Hash Table Using Chaining


class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        """Insert a key-value pair into the hash table."""
        index = self._hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                print(f"Updated key {key} with value {value}.")
                return
        self.table[index].append([key, value])
        print(f"Inserted key {key} with value {value}.")

    def search(self, key):
        """Search for a value by key in the hash table."""
        index = self._hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None

    def delete(self, key):
        """Delete a key-value pair from the hash table."""
        index = self._hash_function(key)
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                del self.table[index][i]
                print(f"Deleted key {key}.")
                return
        print(f"Key {key} not found.")

    def display(self):
        """Display the hash table."""
        for i, bucket in enumerate(self.table):
            print(f"Bucket {i}: {bucket}")

# Usage
hash_table = HashTable()
hash_table.insert("apple", 10)
hash_table.insert("banana", 20)
hash_table.insert("grape", 30)
hash_table.display()

print("Search for 'apple':", hash_table.search("apple"))  # Output: 10
hash_table.delete("banana")
hash_table.display()
