# finds max number in a given array

# O(N) time


input = [3, 5, 6, 1, 2, 4]


def find_max_num(array):
    temp = array[0]
    for n in array:
        temp = n if n > temp else temp

    return temp


result = find_max_num(input)
print(result)
