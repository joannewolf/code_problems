# Number Guessing
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000051060/00000000000588f4

import sys

T = int(input())
for t in range(T):
    [A, B] = [int(n) for n in input().split()]
    N = int(input())

    l = A + 1
    r = B
    for i in range(N):
        mid = (l + r) // 2
        print(mid)
        sys.stdout.flush()
        reply = input()
        if reply == "CORRECT":
            break
        elif reply == "TOO_SMALL":
            l = mid + 1
        elif reply == "TOO_BIG":
            r = mid - 1
