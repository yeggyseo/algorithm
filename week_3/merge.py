# merge sort helper function

# O(n) time


array_a = [1, 2, 3, 5]
array_b = [4, 6, 7, 8]


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


print(merge(array_a, array_b))  # [1, 2, 3, 4, 5, 6, 7, 8] 가 되어야 합니다!