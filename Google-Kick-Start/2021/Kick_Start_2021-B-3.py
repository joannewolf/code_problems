# Consecutive Primes
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435a5b/000000000077a8e6
# Pass test set 2, MLE for calculating all primes <= 10^9

import math

MAX_NUM = pow(10, 6)
nums = set(range(3, MAX_NUM, 2))
primes = [2]
flag = 3
while nums and flag <= MAX_NUM:
    if flag in nums:
        primes.append(flag)
        for i in range(1, MAX_NUM // flag + 1, 2):
            nums.discard(flag * i)
    flag += 2
# print(len(primes))
# print(primes)

T = int(input())
for t in range(T):
    Z = int(input())

    l = 0
    r = len(primes) - 1
    while l <= r:
        mid = (l + r) // 2
        if primes[mid] <= math.sqrt(Z):
            l = mid + 1
        else:
            r = mid - 1
    # print(l, r, primes[r])

    if primes[r] * primes[r + 1] <= Z:
        result = primes[r] * primes[r + 1]
    else:
        result = primes[r] * primes[r - 1]
    print("Case #{}: {}".format(t + 1, result))
