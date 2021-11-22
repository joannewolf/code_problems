# Perfect Subarray
# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff43/00000000003381cb
# O(N^2), TLE on test set 2

import math

T = int(input())
for t in range(T):
    N = int(input())
    num = [int(n) for n in input().split()]

    sum = [0]
    for i in range(N):
        sum.append(num[i] + sum[-1])
    # print(sum)

    ans = 0
    for i in range(N):
        for j in range(i, N):
            sub_sum = sum[j + 1] - sum[i]
            if sub_sum >= 0 and math.sqrt(sub_sum) == int(math.sqrt(sub_sum)):
                # print(i, j, sub_sum)
                ans += 1

    print(f"Case #{t + 1}: {ans}")
