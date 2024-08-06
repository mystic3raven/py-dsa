def exponential_search(arr, target):
    """Perform exponential search for the target in a sorted array."""
    if arr[0] == target:
        return 0

    n = len(arr)
    index = 1

    while index < n and arr[index] <= target:
        index *= 2

    return binary_search_recursive(arr, target, index // 2, min(index, n - 1))

# Usage
arr = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
target = 32
index = exponential_search(arr, target)
print(f"Element {target} found at index {index}.")  # Output: Element 32 found at index 5.
