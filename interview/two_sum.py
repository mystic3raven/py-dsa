
'''
This code uses a dictionary (seen) to store the numbers encountered so far and their indices. 
For each number in the array, it calculates the complement needed to reach the target.
If the complement is found in the dictionary, it means the pair has been found, and their indices are returned. Otherwise, 
the current number and its index are added to the dictionary.

This solution has a time complexity of O(n) because it iterates through the array only once.
The space complexity is also O(n) in the worst case, as the dictionary may store all the numbers in the array.

'''


def two_sum(nums, target):
    """
    Finds the indices of two numbers in an array that add up to a given target.

    Args:
      nums: An array of integers.
      target: The target sum.

    Returns:
      A list containing the indices of the two numbers, or an empty list if no such pair exists.
    """
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

# Example usage
nums = [2, 7, 11, 15]
target = 9
indices = two_sum(nums, target)
print(indices)  # Output: [0, 1]

