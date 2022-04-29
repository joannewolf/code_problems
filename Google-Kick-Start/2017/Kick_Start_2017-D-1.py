# Sightseeing
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000201b77/0000000000201bfd
# DP, TLE but correct locally on test set 2

import math

INF = pow(10, 10)

# The max # of sightseeing if reach city i at sec start
def go(start, i):
    # print("start", start, "i", i)
    if i == N - 1:
        if start > T_F:
            return -INF
        else:
            return 0
    
    if (start, i) in dp:
        return dp[(start, i)]
    
    (S, F, D) = bus[i]
    # Go without sightseeing city i
    x = max(math.ceil((start - S) / F), 0)
    # print("option 1", x)
    option1 = go(S + x * F + D, i + 1)
    # Go with sightseeing city i
    # print("option 2", x)
    x = max(math.ceil((start + T_S - S) / F), 0)
    option2 = 1 + go(S + x * F + D, i + 1)

    dp[(start, i)] = max(option1, option2)
    return dp[(start, i)]


T = int(input())
for t in range(T):
    [N, T_S, T_F] = [int(x) for x in input().split()]
    bus = []
    for _ in range(N-1):
        [s, f, d] = [int(x) for x in input().split()]
        bus.append((s, f, d))

    dp = {}

    ans = go(0, 0)
    if ans < 0:
        print(f"Case #{t + 1}: IMPOSSIBLE")
    else:
        print(f"Case #{t + 1}: {ans}")
