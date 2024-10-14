'''
This code uses a sliding window approach with two pointers, start and end, and a dictionary char_index to store
the last seen index of each character. It iterates through the string, 
expanding the window (end) until a repeating character is found. When a repeating character is encountered, 
the window is shifted to the right (start) by one position past the previous occurrence of the character. 
The maximum length of the substring without repeating characters is updated during this process.

This solution has a time complexity of O(n), where n is the length of the string, as each character 
is visited at most twice. The space complexity is O(min(n, m)), where m is the size of the character set, as the dictionary 
stores the last seen index of each character.

'''

def length_of_longest_substring(s):
    """
    Finds the length of the longest substring without repeating characters.

    Args:
      s: The input string.

    Returns:
      The length of the longest substring without repeating characters.
    """
    start = 0
    end = 0
    max_len = 0
    char_index = {}

    for end in range(len(s)):
        if s[end] in char_index and char_index[s[end]] >= start:
            start = char_index[s[end]] + 1
        char_index[s[end]] = end
        max_len = max(max_len, end - start + 1)

    return max_len 1 

# Example usage
s = "abcabcbb"
length = length_of_longest_substring(s)
print(length)  # Output: 3

s = "bbbbb"
length = length_of_longest_substring(s)
print(length)  # Output: 1

s = "pwwkew"
length = length_of_longest_substring(s)
print(length)  # Output: 3


