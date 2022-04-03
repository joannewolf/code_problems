# Twisty Little Passages
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000876ff1/0000000000a45fc0

import sys
import random

T = int(input())
for t in range(T):
    [N, K] = [int(x) for x in input().split()]
    [R1, P1] = [int(x) for x in input().split()]
    edge = {}
    edge[R1] = P1
    estimate = 0
    for i in range(0, K, 2):
        room = random.randint(1, N)
        print(f"T {room}")
        sys.stdout.flush()
        [R, P_T] = [int(x) for x in input().split()]
        edge[R] = P_T
        estimate += P_T
        print(f"W")
        sys.stdout.flush()
        [R, P_W] = [int(x) for x in input().split()]
        edge[R] = P_W
    estimate //= (K // 2)

    sum = 0
    for i in range(1, N+1):
        if i in edge:
            sum += edge[i]
        else:
            sum += estimate

    print(f"E {sum // 2}")
    sys.stdout.flush()
