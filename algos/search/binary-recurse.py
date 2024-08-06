def binary_search_recursive(arr, target, left, right):
    """Perform recursive binary search for the target in a sorted array."""
    if left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return binary_search_recursive(arr, target, mid + 1, right)
        else:
            return binary_search_recursive(arr, target, left, mid - 1)
    return -1

# Usage
arr = [1, 2, 3, 4, 5, 6, 7]
target = 5
index = binary_search_recursive(arr, target, 0, len(arr) - 1)
print(f"Element {target} found at index {index}.")  # Output: Element 5 found at index 4.
