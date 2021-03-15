# Finds the most used alphabet in a string
# using ASCII, convert char to ord and vise versa
# to count the most occurred alphabet

# O(N) time
# θ(N) space

def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0] * 26

    for c in string:
        if c.isalpha():
            arr_index = ord(c) - ord("a")
            alphabet_occurrence_array[arr_index] += 1

    i = 0
    max = alphabet_occurrence_array[0]

    for n in range(len(alphabet_occurrence_array)):
        if alphabet_occurrence_array[n] > max:
            max = alphabet_occurrence_array[n]
            i = n

    return chr(i + ord("a"))

print(find_alphabet_occurrence_array("what is good my friends!"))



