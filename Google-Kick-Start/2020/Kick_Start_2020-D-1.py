# Record Breaker
# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff08/0000000000387171

import sys
import math

T = int(input())
for t in range(T):
    N = int(input())
    visitor = [int(n) for n in input().split()]

    ans = 0
    max_visitor = -1
    for i in range(N):
        if visitor[i] > max_visitor and (i == N - 1 or visitor[i] > visitor[i + 1]):
            ans += 1
        max_visitor = max(max_visitor, visitor[i])

    print(f"Case #{t + 1}: {ans}")
