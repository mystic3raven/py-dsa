
    """
    This code uses three pointers: p1 for nums1, p2 for nums2, and p for the merged array (which is nums1 itself). It starts from the end of both arrays and compares the elements, placing the larger element at the end of nums1. After one of the arrays is exhausted, the remaining elements from the other array are copied to nums1.

This solution has a time complexity of O(m + n), as it iterates through both arrays once. The space complexity is O(1), as it modifies nums1 in place.

    Returns:
        _type_: _description_
    """

import heapq

def maxScore(nums, k):
    """
    Calculates the maximum possible score attainable after applying k operations.

    Args:
      nums: A 0-indexed integer array.
      k: The number of operations allowed.

    Returns:
      The maximum possible score.
    """
    score = 0
    heap = [-num for num in nums]  # Use negative values for max-heap
    heapq.heapify(heap)

    for _ in range(k):
        num = -heapq.heappop(heap)
        score += num
        heapq.heappush(heap, -math.ceil(num / 3))

    return score

# Example usage
nums = [10, 10, 10, 10, 10]
k = 5
result = maxScore(nums, k)
print(result)  # Output: 50

nums = [1, 10, 3, 3, 3]
k = 3
result = maxScore(nums, k)
print(result)  # Output: 17

