# Golf Gophers
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000051635/0000000000104f1a

# There are 7 primes [2, 3, 5, 7, 11, 13, 17] which < 18, if we send all blades as same prime, we'll get the sum of respond as remainder
# G = 2 * x1 + res1 = 3 * x2 + res2 = 5 * x3 + res3 = ...
# Then we can find the number which satisfy this remainder combinations
# but 2*3*5*7*11*13*17 = 510510, and G <= 10^6, we cannot differenciate 489490 and 1000000
# As long as the 7 numbers are relatively prime, it will work
# Use 4 to replace 2, 4*3*5*7*11*13*17 = 1021020, which can cover 10^6

import sys

[T, N, M] = [int(n) for n in input().split()]
primes = [4, 3, 5, 7, 11, 13, 17]
for t in range(int(T)):
    result = 1
    remainder = []
    for i in range(7):
        print(' '.join([str(primes[i])] * 18))
        sys.stdout.flush()
        respond = [int(n) for n in input().split()]
        respond_sum = sum(respond)
        if (respond_sum > result):
            result = respond_sum
        remainder.append(respond_sum % primes[i])
    # print(remainder)

    temp = 1
    for i in range(7):
        while (result % primes[i] != remainder[i]):
            result += temp
        temp *= primes[i]
        # print(result, temp)

    print(result)
    sys.stdout.flush()
    ans = int(input())
    if (ans == 1):
        continue
    elif (ans == -1):
        sys.exit(1)