def heap_sort(array):
    if len(array) == 1 or len(array) == 0: return array
    sorted_array = array.copy()

    def heapify(length_, i_):
        largest = i_
        left = 2 * i_ + 1
        right = 2 * i_ + 2

        if left < length_ and sorted_array[left] > sorted_array[largest]: largest = left
        if right < length_ and sorted_array[right] > sorted_array[largest]: largest = right
        if largest != i_:
            sorted_array[i_], sorted_array[largest] = sorted_array[largest], sorted_array[i_]
            heapify(length_, largest)

    length = len(sorted_array)
    for i in range(length // 2 - 1, -1, -1): heapify(length, i)

    for end in range(length - 1, 0, -1):
        sorted_array[0], sorted_array[end] = sorted_array[end], sorted_array[0]
        heapify(end, 0)

    return sorted_array