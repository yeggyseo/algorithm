# merge sort

#


array = [5, 3, 2, 1, 6, 8, 7, 4]


def merge_sort(array):
    mid = len(array) // 2
    if len(array) <= 1:
        return array
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])
    print(array)
    print(f'left: {left}')
    print(f'right: {right}')
    return merge(left, right)


def merge(array1, array2):
    res = []
    a1 = 0
    a2 = 0

    while a1 < len(array1) and a2 < len(array2):
        if array1[a1] < array2[a2]:
            res.append(array1[a1])
            a1 += 1
        else:
            res.append(array2[a2])
            a2 += 1

    if a1 == len(array1):
        while a2 < len(array2):
            res.append(array2[a2])
            a2 += 1
    if a2 == len(array2):
        while a1 < len(array1):
            res.append(array1[a1])
            a1 += 1
    return res


print(merge_sort(array))  # [1, 2, 3, 4, 5, 6, 7, 8] 가 되어야 합니다!