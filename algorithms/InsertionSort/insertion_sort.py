def insertion_sort (array):
    if len(array) == 0:
        return []
    if len(array) == 1:
        return array
    sorted_array = array.copy()

    for i in range(1, len(sorted_array)):
        key = sorted_array[i]
        j = i - 1

        while j >= 0 and sorted_array[j] > key:
            sorted_array[j + 1] = sorted_array[j]
            j -= 1
        sorted_array[j + 1] = key

    return sorted_array