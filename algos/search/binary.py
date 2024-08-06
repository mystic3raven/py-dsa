def binary_search_iterative(arr, target):
    """Perform iterative binary search for the target in a sorted array."""
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Usage
arr = [1, 2, 3, 4, 5, 6, 7]
target = 5
index = binary_search_iterative(arr, target)
print(f"Element {target} found at index {index}.")  # Output: Element 5 found at index 4.
