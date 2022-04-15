# Square Counting
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000201c97/0000000000201d25
# O(N), TLE on test set 2
# In a square of length n, it can fit n differnt angle of squares which have all four dots on the edge
# Imaging on left edge, square dot split it to (0, n), (1, n-1), (2, n-2), ..., (n-1, 1) => total n different rotation
# And totally there are (R - n) * (C - n) of length-n squares

MOD = pow(10, 9) + 7

T = int(input())
for t in range(T):
    [R, C] = [int(x) for x in input().split()]

    ans = 0
    for n in range(1, min(R, C)):
        ans += (R - n) * (C - n) * n % MOD

    print(f"Case #{t + 1}: {ans % MOD}")
