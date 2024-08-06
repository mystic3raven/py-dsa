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
    
    def delete(self, word):
    """Delete a word from the trie."""
        def _delete(node, word, depth):
            if not node:
                return False

            # If the last character of the word is being processed
            if depth == len(word):
                # This node is no longer end of word
                if node.is_end_of_word:
                    node.is_end_of_word = False
                    print(f"Deleted '{word}' from the trie.")
                    # If the node has no children, return True to delete it
                    return len(node.children) == 0
                return False

            char = word[depth]
            if char in node.children:
                should_delete = _delete(node.children[char], word, depth + 1)
                if should_delete:
                    del node.children[char]
                    # Return True if no children left and not end of another word
                    return len(node.children) == 0 and not node.is_end_of_word

        return False

    _delete(self.root, word, 0)

# Extend the Trie class with the delete method
Trie.delete = delete

# Usage
trie.delete("hi")
print("Search for 'hi':", trie.search("hi"))  # Output: False
print("Starts with 'hi':", trie.starts_with("hi"))  # Output: False


# Usage
trie = Trie()
trie.insert("hello")
trie.insert("world")

print("Search for 'hello':", trie.search("hello"))  # Output: True
print("Search for 'hell':", trie.search("hell"))    # Output: False
