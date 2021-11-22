# Birthday Cake
# https://codingcompetitions.withgoogle.com/kickstart/round/000000000043585c/000000000085a285

import math

T = int(input())
for t in range(T):
    [R, C, K] = [int(n) for n in input().split()]
    [r1, c1, r2, c2] = [int(n) for n in input().split()]

    L = r2 - r1 + 1
    W = c2 - c1 + 1
    r_cut = math.ceil(L / K)
    c_cut = math.ceil(W / K)

    # Consider only the delicious part itself, how many cuts to divide each cell
    # First divide whole rectangle into smaller squares or rectangles which length or width <= K, and create least number of them
    # So there will be (L // K) * (W // K) squares of length K; if W % K != 0 or L % K != 0, there will be smaller rectangles on the side
    # Inside each smaller squares or rectangles, the cuts needed for #-shape is (n * m - 1)
    #     Cut one direction first, then cut the other direction one cell at a time
    #     (m - 1) + (n - 1) * m == (n - 1) + (m - 1) * n = (n * m - 1)
    result = r_cut * (c_cut + 1) + c_cut * (r_cut + 1) + (K * K - 1) * (L // K) * (W // K)
    if W % K != 0:
        result += (K * (W % K) - 1) * (L // K)
    if L % K != 0:
        result += (K * (L % K) - 1) * (W // K)
    if W % K != 0 and L % K != 0:
        result += (W % K) * (L % K) - 1

    # If any edge of delicious part is on cake edge, then no need to cut that side
    if r1 == 1:
        result -= c_cut
    if r2 == R:
        result -= c_cut
    if c1 == 1:
        result -= r_cut
    if c2 == C:
        result -= r_cut

    # If no edge of delicious part is on cake edge, need at least one entry point from cake edge
    if r1 != 1 and r2 != R and c1 != 1 and c2 != C:
        result += min(math.ceil(min(c2, C - c1 + 1) / K) - c_cut, math.ceil(min(r2, R - r1 + 1) / K) - r_cut)

    print(f"Case #{t + 1}: {result}")
