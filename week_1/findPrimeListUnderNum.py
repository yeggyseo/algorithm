# finds all prime numbers under a given number
# uses Sieve of Eratosthenes

# O(n * log(log(n))) time


input = 10


def find_prime_list_under_number(number):
    isPrime = [True for i in range(number + 1)]
    i = 2

    while i * i <= number:
        if isPrime[i]:
            for n in range(i * i, number + 1, i):
                isPrime[n] = False
        i += 1

    res = []
    for i in range(2, number + 1):
        if isPrime[i]:
            res.append(i)

    return res


result = find_prime_list_under_number(input)
print(result)