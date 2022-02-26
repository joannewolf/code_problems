# Street Checkers
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050edb/00000000001707b9
# Do prime factorization on X = 2^N * 3^m3 * 5^m5 * ...
# The number of factors of X = (N+1) * (m3+1) * (m5+1) ... = (N+1) * M
# And within those factors, only M of them are odd number with no 2's, the rest M * N are even number
# So the legit cases are as below:
#   1. When M = 1 (i.e. no odd prime factor), N can be 0~3 => X can be 1, 2, 4, 8
#   2. When M = 2 (i.e. X is odd prime), N can be 0~2
#   3. When M > 2, N can only be 1
# => Odd integer except 1 * 2, i.e. 2 * (2x + 1) = 4x + 2, x >= 1 || prime number including 1 || prime number including 1 * 4

import math

def count_prime(L: int, R: int):
    nums = set(range(L+1, R+1))
    primes = set(range(2, int(math.sqrt(R)) + 1))
    for i in range(2, int(math.sqrt(R)) + 1):
        if i in primes:
            for j in range(int(math.sqrt(R)) // i - i + 1):
                primes.discard(i * (i + j))
            for j in range(max(L // i - i, 0), R // i - i + 1):
                nums.discard(i * (i + j))
    # print(nums)

    return len(nums)

T = int(input())
for t in range(T):
    [L, R] = [int(n) for n in input().split()]

    ans = 0
    ans += max(((R - 2) // 4), 0) - max((L - 1 - 2) // 4, 0)
    ans += count_prime(L - 1, R)
    ans += count_prime((L - 1) // 4, R // 4)

    print(f"Case #{t + 1}: {ans}")
