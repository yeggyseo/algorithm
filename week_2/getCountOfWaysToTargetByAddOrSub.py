# counts total number of ways to get target number from a given array,
# only using addition and subtraction. Using DP

# O(n * m) time? might be wrong :|


numbers = [1, 1, 1, 1, 1]
target_number = 3


def get_count_of_ways_to_target_by_doing_plus_or_minus(array, target):
    s = 0
    for n in array:
        s += n

    if target > s or (target + s) % 2 == 1:
        return 0

    dp = [0] * int(((target + s) / 2 + 1))
    dp[0] = 1

    for n in array:
        i = len(dp) - 1
        while i >= n:
            dp[i] += dp[i - n]
            i -= 1
    return dp[len(dp) - 1]


print(get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, target_number))
