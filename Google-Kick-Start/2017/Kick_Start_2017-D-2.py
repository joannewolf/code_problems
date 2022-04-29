# Sherlock and Matrix Game
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000201b77/0000000000201c95
# O(N^4*logK), TLE on test set 2

import heapq

T = int(input())
for t in range(T):
    [N, K, A1, B1, C, D, E1, E2, F] = [int(x) for x in input().split()]
    A = [A1]
    B = [B1]
    x = A1
    y = B1
    r = 0
    s = 0
    for _ in range(N-1):
        new_x = (C * x + D * y + E1) % F
        new_y = (D * x + C * y + E2) % F
        new_r = (C * r + D * s + E1) % 2
        new_s = (D * r + C * s + E2) % 2
        A.append(pow(-1, new_r) * new_x)
        B.append(pow(-1, new_s) * new_y)
        x = new_x
        y = new_y
        r = new_r
        s = new_s
    # print(A)
    # print(B)
    prefix_A = [0]
    prefix_B = [0]
    for i in range(N):
        prefix_A.append(prefix_A[-1] + A[i])
        prefix_B.append(prefix_B[-1] + B[i])

    pq = [] # Priority queue of top-K element
    # submatrix of row [i1, j1] and column [i2, j2], inclusive
    for i1 in range(N):
        for j1 in range(i1, N):
            for i2 in range(N):
                for j2 in range(i2, N):
                    temp = (prefix_A[j1+1] - prefix_A[i1]) * (prefix_B[j2+1] - prefix_B[i2])
                    if len(pq) < K:
                        heapq.heappush(pq, temp)
                    elif pq[0] < temp:
                        heapq.heapreplace(pq, temp) # Equal operation as pop than push

    print(f"Case #{t + 1}: {pq[0]}")
