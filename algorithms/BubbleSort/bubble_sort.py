def bubble_sort(array):
    if len(array) == 1 or len(array) == 0:
        return array

    sorted_array = array.copy()
    length = len(sorted_array)

    while True:
        swapped = False
        for i in range(1, length):
            if sorted_array[i - 1] > sorted_array[i]:
                sorted_array[i - 1], sorted_array[i] = sorted_array[i], sorted_array[i - 1]
                swapped = True
        if not swapped:
            break
        length -= 1

    return sorted_array