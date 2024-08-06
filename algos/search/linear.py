def linear_search(arr, target):
    """Perform linear search for the target in arr."""
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1

# Usage
arr = [3, 5, 2, 4, 9]
target = 4
index = linear_search(arr, target)
print(f"Element {target} found at index {index}.")  # Output: Element 4 found at index 3.
