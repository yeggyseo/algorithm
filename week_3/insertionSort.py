# insertion sort
# O(n^2) time, O(n) best time


input = [4, 6, 2, 9, 1]


def insertion_sort(array):
    n = len(array)

    for i in range(1, n):
        for j in range(i):
            if array[i - j - 1] > array[i - j]:
                array[i - j - 1], array[i - j] = array[i - j], array[i - j - 1]
            else:
                break
    return array

print(insertion_sort(input))
