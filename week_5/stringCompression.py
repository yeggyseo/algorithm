input = "abcabcabcabcdededededede"


def string_compression(string):
    n = len(string)
    length = []

    for splitSize in range(1, n // 2 + 1):
        splitted = [string[i:i + splitSize] for i in range(0, n, splitSize)]

        compressed = ""
        count = 1

        for j in range(1, len(splitted)):
            prev, cur = splitted[j - 1], splitted[j]

            if prev == cur:
                count += 1
            else:
                if count > 1:
                    compressed += (str(count) + prev)
                else:
                    compressed += prev
                count = 1

        if count > 1:
            compressed += (str(count) + splitted[-1])
        else:
            compressed += splitted[-1]

        length.append(len(compressed))

    return min(length)


print(string_compression(input))