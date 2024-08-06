def bucket_sort(arr):
    if len(arr) == 0:
        return

    bucket_count = 10
    max_val = max(arr)
    buckets = [[] for _ in range(bucket_count)]

    for num in arr:
        index = int(num / max_val * (bucket_count - 1))
        buckets[index].append(num)

    for bucket in buckets:
        bucket.sort()

    k = 0
    for bucket in buckets:
        for num in bucket:
            arr[k] = num
            k += 1

# Usage
arr = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]
bucket_sort(arr)
print("Bucket Sorted array:", arr)
