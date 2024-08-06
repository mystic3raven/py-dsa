def fibonacci_search(arr, target):
    """Perform Fibonacci search for the target in a sorted array."""
    n = len(arr)
    fib2, fib1 = 0, 1
    fib = fib1 + fib2

    while fib < n:
        fib2 = fib1
        fib1 = fib
        fib = fib1 + fib2

    offset = -1

    while fib > 1:
        i = min(offset + fib2, n - 1)

        if arr[i] < target:
            fib = fib1
            fib1 = fib2
            fib2 = fib - fib1
            offset = i
        elif arr[i] > target:
            fib = fib2
            fib1 -= fib2
            fib2 = fib - fib1
        else:
            return i

    if fib1 and offset < n - 1 and arr[offset + 1] == target:
        return offset + 1

    return -1

# Usage
arr = [1, 3, 4, 5, 9, 10]
target = 5
index = fibonacci_search(arr, target)
print(f"Element {target} found at index {index}.")  # Output: Element 5 found at index 3.
