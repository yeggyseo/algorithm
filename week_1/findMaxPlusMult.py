# finds the maximum value in a given array by using + or *

# O(N) time

input = [0, 3, 5, 6, 1, 2, 4]


def find_max_plus_or_multiply(array):
    res = 0

    for n in range(1, len(array)):
        val = array[n]

        if res <= 1 or val <= 1:
            res += val
        else:
            res *= val

    return res


result = find_max_plus_or_multiply(input)
print(result)