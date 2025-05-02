def selection_sort(array):
    if len(array) == 0:
        return []
    if len(array) == 1:
        return array
    sorted_array = array.copy()

    for i in range(len(sorted_array)):
        for j in range(i+1, len(sorted_array)):
            if sorted_array[i] > sorted_array[j]:
                sorted_array[i], sorted_array[j] = sorted_array[j], sorted_array[i]
    return sorted_array