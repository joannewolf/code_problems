# Twisty Little Passages
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000876ff1/0000000000a45fc0
# WA, simply teleport to a randomly-chosen subset of the rooms, calculate the average edges, and assume it's a good estimate of the average edges of all the rooms
# Cons: When most rooms have low degree, and a small set of rooms have high degree — few enough that we are unlikely to find one of them by teleporting randomly
# If these rooms contribute a significant fraction of the total edges, then they must connect to a significant fraction of rooms. So we can find these with high probability by repeatedly teleporting to a random room and then walking through a random passage with the "W" command

import sys

T = int(input())
for t in range(T):
    [N, K] = [int(x) for x in input().split()]
    E = 0
    [R1, P1] = [int(x) for x in input().split()]
    E += P1
    for i in range(1, min(N+1, K+1)):
        if i == R1:
            continue
        print(f"T {i}")
        sys.stdout.flush()
        [R, P] = [int(x) for x in input().split()]
        E += P
    if N <= K:
        print(f"E {E // 2}")
    else:
        print(f"E {E // K * N // 2}")
    sys.stdout.flush()
