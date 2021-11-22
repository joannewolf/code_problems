# Inconstant Ordering
# https://codingcompetitions.withgoogle.com/codejamio/round/00000000004360f2/00000000007772ed

import string

T = int(input())
for t in range(T):
    N = int(input())
    L = [int(n) for n in input().split()]

    result = "A"
    for i in range(0, N, 2):
        if i + 1 == N:
            result += string.ascii_uppercase[1 : L[i] + 1]
        elif L[i+1] < L[i]:
            result += string.ascii_uppercase[1 : L[i] + 1]
            result += string.ascii_uppercase[L[i+1] - 1 : : -1]
        else:
            result += string.ascii_uppercase[1 : L[i]]
            result += string.ascii_uppercase[L[i+1] : : -1]

    print(f"Case #{t + 1}: {result}")
