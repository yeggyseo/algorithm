# Selection sort
# O(n^2) time

input = [4, 6, 2, 9, 1]


def selection_sort(array):
    n = len(array)
    for i in range(n - 1):
        m = i
        for j in range(n - i):
            if array[i + j] < array[m]:
                m = i + j
        array[i], array[m] = array[m], array[i]
    return array


print(selection_sort(input))
