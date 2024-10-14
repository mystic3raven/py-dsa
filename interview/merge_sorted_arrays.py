def merge(nums1, m, nums2, n):
    """
    Merges two sorted arrays into a single sorted array.

    Args:
      nums1: The first sorted array.
      m: The number of elements in nums1.
      nums2: The second sorted array.
      n: The number of elements in nums2.   
    """
    p1 = m - 1
    p2 = n - 1
    p = m + n - 1

    while p1 >= 0 and p2 >= 0:
        if nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1

    # Copy remaining elements from nums2   
    nums1[:p2 + 1] = nums2[:p2 + 1]

# Example usage
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
merge(nums1, m, nums2, n)
print(nums1)  # Output: [1, 2, 2, 3, 5, 6]

'''
This code uses three pointers: p1 for nums1, p2 for nums2, and p for the merged array (which is nums1 itself). It starts from the end of both arrays and compares the elements, placing the larger element at the end of nums1. After one of the arrays is exhausted, the remaining elements from the other array are copied to nums1.

This solution has a time complexity of O(m + n), as it iterates through both arrays once. The space complexity is O(1), as it modifies nums1 in place.

'''