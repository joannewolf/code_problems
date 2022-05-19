# Cake
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000201d29/0000000000201d2a

import math

MAX_INT = 10000

T = int(input())
for t in range(T):
    N = int(input())

    ans = 0
    dp = [MAX_INT] * (N + 1)
    # dp[i]: the minimum # cakes to reach i cm^2

    for i in range(1, N+1):
        if i == int(math.sqrt(i)) * int(math.sqrt(i)):
            dp[i] = 1
        else:
            for j in range(1, int(math.sqrt(i)) + 1):
                dp[i] = min(dp[i], 1 + dp[i - j * j])

    print(f"Case #{t + 1}: {dp[N]}")
