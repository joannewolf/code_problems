# Consecutive Primes
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435a5b/000000000077a8e6

import math

def is_prime(n):
    # 6k ± 1 optimization, https://en.wikipedia.org/wiki/Primality_test
    if n <= 3:
        return (n > 1)
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while pow(i, 2) <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

T = int(input())
for t in range(T):
    Z = int(input())

    if (Z < 15):
        print("Case #{}: 6".format(t + 1))
        continue

    # Find first 2 primes <= sqrt(Z) and first prime > sqrt(Z)
    max_gap = 300 # https://en.wikipedia.org/wiki/Prime_gap
    primes = [-1] * 3
    root = math.floor(math.sqrt(Z)) if math.floor(math.sqrt(Z)) % 2 == 1 else math.floor(math.sqrt(Z)) - 1
    # print(root)
    for i in range(root, root - 2 * max_gap, -2):
        if is_prime(i):
            if primes[1] == -1:
                primes[1] = i
            elif primes[0] == -1:
                primes[0] = i
                break
    for i in range(root + 2, root + max_gap, 2):
        if is_prime(i):
            primes[2] = i
            break

    # print(primes)
    if (primes[1] * primes[2] <= Z):
        result = primes[1] * primes[2]
    else:
        result = primes[0] * primes[1]

    print("Case #{}: {}".format(t + 1, result))
