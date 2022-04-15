# Square Counting
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000201c97/0000000000201d25
# O(N), TLE on test set 2
# In a square of length n, it can fit n differnt angle of squares which have all four dots on the edge
# Imaging on left edge, square dot split it to (0, n), (1, n-1), (2, n-2), ..., (n-1, 1) => total n different rotation
# And totally there are (R - n) * (C - n) of length-n squares
# SUM{(R - i) * (C - i) * i} = SUM{ RCi - (R+C)i^2 + i^3}, i = 1 ~ min(R, C)
# = RCn(n+1)/2 - (R+C)n(n+1)(2n+1)/6 + (n(n+1)/2)^2

MOD = pow(10, 9) + 7
INV3 = (MOD + 1) // 3

T = int(input())
for t in range(T):
    [R, C] = [int(x) for x in input().split()]

    n = min(R, C)
    part = n * (n + 1) // 2 % MOD

    ans = (R * C * part - (R + C) * part * (2 * n + 1) * INV3 + part * part) % MOD

    print(f"Case #{t + 1}: {ans}")
