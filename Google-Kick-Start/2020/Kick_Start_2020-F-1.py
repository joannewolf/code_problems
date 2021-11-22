# ATM Queue
# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff48/00000000003f4ed8

import math

T = int(input())
for t in range(T):
    [N, X] = [int(n) for n in input().split()]
    money = [int(n) for n in input().split()]

    ans = sorted([(math.ceil(money[i] / X), i + 1) for i in range(N)])
    ans = [index for (_, index) in ans]
    print(f"Case #{t + 1}: {' '.join([str(n) for n in ans])}")
