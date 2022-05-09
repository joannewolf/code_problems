# Infinity Area
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000008caa74/0000000000acf079

import math

T = int(input())
for t in range(T):
    [R, A, B] = [int(x) for x in input().split()]

    ans = 0
    now = R
    flag = True
    while now != 0:
        ans += now * now
        if flag:
            now *= A
        else:
            now //= B
        flag = not flag

    ans *= math.pi
    print(f"Case #{t + 1}: {ans}")
