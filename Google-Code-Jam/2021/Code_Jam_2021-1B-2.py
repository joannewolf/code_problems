# Subtransmutation
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000435baf/00000000007ae4aa

import math

def solve(H, D):
    while H and D:
        # Remove intersection elements
        intersection = H.keys() & D.keys()
        for key in intersection:
            if H[key] > D[key]:
                H[key] -= D[key]
                D.pop(key)
            elif H[key] == D[key]:
                H.pop(key)
                D.pop(key)
            else:
                D[key] -= H[key]
                H.pop(key)
        if not D:
            return True
        elif not H:
            return False
        # Transform the next biggest element in H
        max_key = max(H.keys())
        if max_key - A > 0:
            if max_key - A in H.keys():
                H[max_key - A] += H[max_key]
            else:
                H[max_key - A] = H[max_key]
        if max_key - B > 0:
            if max_key - B in H.keys():
                H[max_key - B] += H[max_key]
            else:
                H[max_key - B] = H[max_key]
        H.pop(max_key)

    if not D:
        return True
    else:
        return False

T = int(input())
for t in range(T):
    [N, A, B] = [int(n) for n in input().split()]
    U = [int(n) for n in input().split()]

    done = False
    gcd = math.gcd(A, B)
    remainder = N % gcd
    # print(gcd, remainder)
    for i, u in enumerate(U):
        if u > 0 and (i + 1) % gcd != remainder:
            print(f"Case #{t + 1}: IMPOSSIBLE")
            done = True
            break
    if done:
        continue

    # The answer m is not too large based on limits, just iterate to find m
    D = {}
    for i, u in enumerate(U):
        if u > 0:
            D[i + 1] = u
    for m in range(1, 500):
        if solve({m: 1}, D.copy()):
            print(f"Case #{t + 1}: {m}")
            break
