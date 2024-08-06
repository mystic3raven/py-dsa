#
# Segment Tree
# A segment tree is a tree used for storing intervals or segments. It allows querying
# which of the stored segments contain a given point.
# Implementation

# Here's a basic implementation of a segment tree for range sum queries:

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """Insert a word into the trie."""
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.is_end_of_word = True
        print(f"Inserted '{word}' into the trie.")

    def search(self, word):
        """Search for a word in the trie."""
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        return current.is_end_of_word

# Usage
trie = Trie()
trie.insert("hello")
trie.insert("world")

print("Search for 'hello':", trie.search("hello"))  # Output: True
print("Search for 'hell':", trie.search("hell"))    # Output: False
