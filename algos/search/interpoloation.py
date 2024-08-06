import math

def jump_search(arr, target):
    """Perform jump search for the target in a sorted array."""
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0

    while arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1

    for i in range(prev, min(step, n)):
        if arr[i] == target:
            return i
    return -1

# Usage
arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 7
index = jump_search(arr, target)
print(f"Element {target} found at index {index}.")  # Output: Element 7 found at index 7.
