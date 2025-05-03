def bubble_sort(array):
    if len(array) == 1 or len(array) == 0: return array

    sorted_array = array.copy()
    length = len(sorted_array)

    while True:
        swap_pairs = [(i - 1, i) for i in range(1, length) if sorted_array[i - 1] > sorted_array[i]]
        for a, b in swap_pairs:
            sorted_array[a], sorted_array[b] = sorted_array[b], sorted_array[a]
        if not swap_pairs:
            break
    return sorted_array