# summarizes character occurrences
# ex) aaabbbc	# a3/b3/c1

input_str = "acccdeee"


def summarize_string(input_str):
    alphabet = [0] * 26

    for c in input_str:
        if c.isalpha():
            i = ord(c) - ord("a")
            alphabet[i] += 1

    res = ""
    for i in range(len(alphabet)):
        if alphabet[i] == 0:
            continue
        if i != 0:
            res += "/"

        res += "{}{}".format(chr(i + ord("a")), alphabet[i])

    return res


print(summarize_string(input_str))


#### ALTERNATIVE (ASSUMING THE STRING IS SORTED) ####

# def summarize_string(target_string):
#     n = len(target_string)
#     count = 0
#     result_str = ''
#
#     for i in range(n - 1):
#         if target_string[i] == target_string[i + 1]:
#             count += 1
#         else:
#             result_str += target_string[i] + str(count + 1) + '/'
#             count = 0
#
#     result_str += target_string[n - 1] + str(count + 1)
#
#     return result_str
#
#
# input_str = "acccdeee"
#
# print(summarize_string(input_str))