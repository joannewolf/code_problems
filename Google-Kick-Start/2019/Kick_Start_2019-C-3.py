# Catch Some
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050ff2/0000000000150a0d
# The problem can be transform to:
# Within C different colors of dogs, let's say we choose k_i dogs for color i
# Find SUM(k_i) = K, and minimum time = dogs[1][k_1] * 2 + ... + dogs[C][k_C]
# For the last color we choose, we don't need to go back home so no need multipled by 2
# The reason is:
# (1) We don't change to the color that we observe before, cuz that's not optimal
# (2) If we choose to observe color i's j-th dog, it's optimal that we will also observe all dogs before j-th
# (3) The order of color doesn't matter
# DP, O(N^2)

INF = pow(10, 9)
T = int(input())
for t in range(T):
    [N, K] = [int(n) for n in input().split()]
    P = [int(n) for n in input().split()]
    A = [int(n) for n in input().split()]

    dogs = {}
    for i in range(N):
        if A[i] not in dogs:
            dogs[A[i]] = [P[i]]
        else:
            dogs[A[i]].append(P[i])
    dogs = list(dogs.values())
    C = len(dogs) # The # of different colors
    for pos in dogs:
        pos.sort()
    # print(dogs)

    dp = [[[INF] * 2 for j in range(K+1)] for i in range(C+1)]
    for i in range(C+1):
        dp[i][0][0] = 0
        dp[i][0][1] = 0
    # dp[i][j][k]: The min time to observe j dogs with first i colors, k is 0/1 denoting whether decided the last color
    for i in range(1, C+1):
        L = len(dogs[i-1]) # The # of dogs of current color
        for j in range(1, K+1):
            # Observe 0 dog of current color
            min_value1 = dp[i-1][j][0] + 2 * 0
            min_value2 = dp[i-1][j][0] + 0
            min_value3 = dp[i-1][j][1] + 2 * 0
            # Observe 1...L dogs of current color
            for l in range(min(L, j)):
                min_value1 = min(min_value1, dp[i-1][j-l-1][0] + 2 * dogs[i-1][l])
                min_value2 = min(min_value2, dp[i-1][j-l-1][0] + dogs[i-1][l]) # Take current color as last color
                min_value3 = min(min_value3, dp[i-1][j-l-1][1] + 2 * dogs[i-1][l]) # Already decide last color before

            dp[i][j][0] = min_value1
            dp[i][j][1] = min(min_value2, min_value3)

    print(f"Case #{t + 1}: {dp[C][K][1]}")
