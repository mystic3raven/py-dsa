def removeDuplicates(nums):
    """
    Removes duplicates from a sorted array in-place, allowing each unique element to appear at most twice.

    Args:
      nums: The sorted array.

    Returns:
      The number of elements remaining after removing duplicates.
    """
    if len(nums) <= 2:
        return len(nums)

    i = 2
    for j in range(2, len(nums)):
        if nums[j] != nums[i - 2]:
            nums[i] = nums[j]
            i += 1

    return i

# Example usage
nums = [1, 1, 1, 2, 2, 3]
k = removeDuplicates(nums)
print(k)  # Output: 5
print(nums[:k])  # Output: [1, 1, 2, 2, 3]

nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
k = removeDuplicates(nums)
print(k)  # Output: 7
print(nums[:k])  # Output: [0, 0, 1, 1, 2, 3, 3]

    """
    This code uses two pointers, i and j. i keeps track of the position to place the next unique element, while j iterates through the array. It ensures that each unique element appears at most twice by comparing the current element (nums[j]) with the element two positions before i (nums[i - 2]).

Explanation:

    Initialization:
        i = 2: Starts at index 2 because the first two elements can always be included.

    Iteration:
        The loop iterates from index 2 to the end of the array.
        In each iteration:
            If nums[j] is different from nums[i - 2], it means we can include nums[j] to maintain the "at most twice" condition. So, nums[i] is assigned the value of nums[j], and i is incremented.

    Return i:
        After the loop, i represents the number of elements remaining after removing duplicates.

Time and Space Complexity:

    Time Complexity: O(n), where n is the length of the array, as it iterates through the array once.
    Space Complexity: O(1), as it modifies the array in-place with constant extra memory.
    
    """