def quick_sort(array):
    if len(array) == 0:
        return []
    if len(array) == 1 or len(array) == 0:
        return array

    sorted_array = array.copy()
    length = len(sorted_array)

    def _quicksort(lo, hi):
        if lo < hi:
            p = partition(lo, hi)
            _quicksort(lo, p - 1)
            _quicksort(p + 1, hi)

    def partition(lo, hi):
        pivot = sorted_array[hi]
        i = lo
        for j in range(lo, hi):
            if sorted_array[j] <= pivot:
                sorted_array[i], sorted_array[j] = sorted_array[j], sorted_array[i]
                i += 1
        sorted_array[i], sorted_array[hi] = sorted_array[hi], sorted_array[i]
        return i

    _quicksort(0, len(sorted_array) - 1)
    return sorted_array