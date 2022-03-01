# Book Reading
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050e02/000000000018fd0d
# O(M*sqrt(N)), TLE on test set 2

import math

def add_map(map: map, key: int):
    if key not in map:
        map[key] = 1
    else:
        map[key] += 1

T = int(input())
for t in range(T):
    [N, M, Q] = [int(x) for x in input().split()]
    pages = [int(x) for x in input().split()]
    readers = [int(x) for x in input().split()]

    # For each page, find their all factors
    factors = {}
    for p in pages:
        for i in range(1, int(math.sqrt(p)) + 1):
            if p % i == 0:
                add_map(factors, i)
                if p // i != i:
                    add_map(factors, p // i)
    # print(factors)

    ans = 0
    for r in readers:
        ans += N // r
        if r in factors:
            ans -= factors[r]

    print(f"Case #{t + 1}: {ans}")
