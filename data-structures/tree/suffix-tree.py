class SuffixTrieNode:
    def __init__(self):
        self.children = {}
        self.indices = []

class SuffixTrie:
    def __init__(self, text):
        self.root = SuffixTrieNode()
        self.text = text
        self._build_suffix_trie()

    def _build_suffix_trie(self):
        """Build a suffix trie for the given text."""
        for i in range(len(self.text)):
            current_node = self.root
            for j in range(i, len(self.text)):
                char = self.text[j]
                if char not in current_node.children:
                    current_node.children[char] = SuffixTrieNode()
                current_node = current_node.children[char]
                current_node.indices.append(i)
        print("Built suffix trie.")

    def search(self, pattern):
        """Search for the pattern in the suffix trie and return starting indices."""
        current_node = self.root
        for char in pattern:
            if char not in current_node.children:
                return []
            current_node = current_node.children[char]
        return current_node.indices

# Usage
text = "bananas"
suffix_trie = SuffixTrie(text)

# Search for a pattern
pattern = "ana"
indices = suffix_trie.search(pattern)
print(f"Pattern '{pattern}' found at indices: {indices}")  # Output: Pattern 'ana' found at indices: [1, 3]
