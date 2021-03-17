# Uses binary search to check if a target exists in an array

# O(log(n)) time

finding_target = 14
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


def is_existing_target_number_binary(target, array):
    cmin = 0
    cmax = len(array) - 1
    guess = (cmin + cmax) // 2

    while cmin <= cmax:
        if array[guess] == target:
            return True
        elif array[guess] < target:
            cmin = guess + 1
        else:
            cmax = guess - 1
        guess = (cmin + cmax) // 2
    return False


result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)