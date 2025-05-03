def bucket_sort(array, k=10):
    if len(array) == 1 or len(array) == 0: return array

    copy_array = array.copy()
    min_val, max_val = min(copy_array), max(copy_array)
    range_val = (max_val - min_val) or 1

    buckets = [[x for x in array if (x - min_val) * (k - 1) // range_val == idx] for idx in range(k)]
    sorted_array = [item for bucket in buckets for item in sorted(bucket)]

    return sorted_array