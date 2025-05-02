def bucket_sort(array, k=10):
    if len(array) == 1 or len(array) == 0:
        return array

    copy_array = array.copy()
    min_val, max_val = min(copy_array), max(copy_array)
    range_val = (max_val - min_val) or 1
    buckets = [[] for _ in range(k)]

    for x in array:
        idx = (x - min_val) * (k - 1) // range_val
        buckets[idx].append(x)

    sorted_array = []
    for bucket in buckets:
        sorted_array.extend(sorted(bucket))

    return sorted_array