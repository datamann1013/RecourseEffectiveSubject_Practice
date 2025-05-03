def radix_sort(array, base=10):
    if len(array) == 1 or len(array) == 0: return array

    sorted_array = array.copy()
    max_val, exp = max(sorted_array), 1

    while exp <= max_val:
        buckets = [[] for _ in range(base)]

        for num in sorted_array:
            digit = (num // exp) % base
            buckets[digit].append(num)

        sorted_array = []
        for bucket in buckets: sorted_array.extend(bucket)
        exp *= base

    return sorted_array