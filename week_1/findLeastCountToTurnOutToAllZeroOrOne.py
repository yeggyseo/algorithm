# finds the least amount of flips needed to unify
# 0 to 1, or vice versa. Series of numbers can be flipped
# and be counted as 1 flip.

# O(n) time

input = "011110110000110100010101110"


def find_count_to_turn_out_to_all_zero_or_all_one(string):
    zeroCount = 0
    oneCount = 0

    if string[0] == "0":
        oneCount += 1
    else:
        zeroCount += 1

    for i in range(len(string) - 1):
        if string[i] == string[i + 1]:
            continue
        if string[i + 1] == "0":
            oneCount += 1
        else:
            zeroCount += 1

    return min(oneCount, zeroCount)


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)