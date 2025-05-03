def heap_sort(array):
    if len(array) == 1 or len(array) == 0:
        return array

    copy_array = array.copy()

    def heapify(length, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < length and copy_array[left] > copy_array[largest]:
            largest = left

        if right < length and copy_array[right] > copy_array[largest]:
            largest = right

        if largest != i:
            copy_array[i], copy_array[largest] = copy_array[largest], copy_array[i]
            heapify(length, largest)

    length = len(copy_array)
    for i in range(length // 2 - 1, -1, -1):
        heapify(length, i)

    for end in range(length - 1, 0, -1):
        copy_array[0], copy_array[end] = copy_array[end], copy_array[0]
        heapify(end, 0)


    return copy_array