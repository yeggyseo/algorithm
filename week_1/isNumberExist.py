# checks if a number exists in an array

# O(N) time


input = [3, 5, 6, 1, 2, 4]

def is_number_exist(number, array):
    for n in array:
        if n == number:
            return True
    return False


result = is_number_exist(2, input)
print(result)