def merge_sort(array):
    copy_array = array.copy()

    if len(array) == 1 or len(array) == 0:
        return array

    mid = len(copy_array) // 2
    left = merge_sort(copy_array[:mid])
    right = merge_sort(copy_array[mid:])

    sorted_array = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1

    sorted_array.extend(left[i:])
    sorted_array.extend(right[j:])

    return sorted_array