# find the FIRST not repeating character in a string
# Uses ASCII to find the occurrence of all characters
# then appends characters with 1 occurrence to a temp list
# go through the string again and return if a char is in the temp list

# O(N^2) time
# O(N) space


# input = "abacabade"
input = "abadabac"


def find_not_repeating_character(string):
    alphabets = [0] * 26

    for c in string:
        alphabet_index = ord(c) - ord("a")
        alphabets[alphabet_index] += 1

    temp = []
    for n in range(len(alphabets)):
        if alphabets[n] == 1:
            temp.append(chr(n + ord("a")))

    for c in string:
        if c in temp:
            return c


result = find_not_repeating_character(input)
print(result)