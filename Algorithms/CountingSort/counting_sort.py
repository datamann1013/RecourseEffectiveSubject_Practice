def counting_sort(array):
    if len(array) == 1 or len(array) == 0: return array

    sorted_array = array.copy()
    min_val, max_val = min(sorted_array), max(sorted_array)
    length = max_val - min_val + 1
    number_array = [0] * length

    for j in sorted_array: number_array[j - min_val] +=1
    for i in range(1, length): number_array[i] += number_array[i - 1]

    n = len(sorted_array)
    output = [None] * n

    for x in reversed(sorted_array):
        idx = x - min_val
        number_array[idx] -= 1
        output[number_array[idx]] = x

    return output