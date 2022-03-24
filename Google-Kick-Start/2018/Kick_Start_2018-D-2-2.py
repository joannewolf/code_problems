# Paragliding
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050ee1/0000000000051006
# O((N+K)logN)

T = int(input())
for t in range(T):
    [N, K] = [int(x) for x in input().split()]
    [p1, p2, A1, B1, C1, M1] = [int(x) for x in input().split()]
    [h1, h2, A2, B2, C2, M2] = [int(x) for x in input().split()]
    [x1, x2, A3, B3, C3, M3] = [int(x) for x in input().split()]
    [y1, y2, A4, B4, C4, M4] = [int(x) for x in input().split()]

    P = [p1, p2]
    H = [h1, h2]
    X = [x1, x2]
    Y = [y1, y2]
    for i in range(2, N):
        next_p = (P[-1] * A1 + P[-2] * B1 + C1) % M1 + 1
        P.append(next_p)
        next_h = (H[-1] * A2 + H[-2] * B2 + C2) % M2 + 1
        H.append(next_h)
    for i in range(2, K):
        next_x = (X[-1] * A3 + X[-2] * B3 + C3) % M3 + 1
        X.append(next_x)
        next_y = (Y[-1] * A4 + Y[-2] * B4 + C4) % M4 + 1
        Y.append(next_y)
    # print(P)
    # print(H)
    # print(X)
    # print(Y)

    # Optimization idea: if H[i] <= H[j] - abs(P[i] - P[j]), means any balloon reachable by i can be also reached by j
    # So remove those towers which can be covered by others
    # O(NlogN + N)
    towers = []
    key_towers = []
    for i in range(N):
        towers.append((P[i], H[i]))
    towers.sort()
    flag = 0
    while flag < N:
        if key_towers and towers[flag][1] <= key_towers[-1][1] - abs(towers[flag][0] - key_towers[-1][0]):
            flag += 1
        else:
            while key_towers:
                if key_towers[-1][1] <= towers[flag][1] - abs(towers[flag][0] - key_towers[-1][0]):
                    key_towers.pop(-1)
                else:
                    break
            key_towers.append(towers[flag])

    # After tower optimization, for each balloon, if it can be collected, it must be the closest tower
    # Use binary search to find the closest tower of each balloon
    # O(KlogN)
    ans = 0
    N2 = len(key_towers)
    for i in range(K):
        l, r = 0, N2 - 1
        while l <= r:
            mid = (l + r) // 2
            if key_towers[mid][0] <= X[i]:
                l = mid + 1
            else:
                r = mid - 1
        # final R is max element index which <= target
        # final L is min element index which > target
        if r == -1: # Balloon is on left side of all towers
            if key_towers[0][1] >= Y[i] + (key_towers[0][0] - X[i]):
                ans += 1
        elif l == N2: # Balloon is on right side of all towers
            if key_towers[-1][1] >= Y[i] + (X[i] - key_towers[-1][0]):
                ans += 1
        else:
            if (key_towers[l][1] >= Y[i] + (key_towers[l][0] - X[i]) or
                key_towers[r][1] >= Y[i] + (X[i] - key_towers[r][0])):
                ans += 1

    print(f"Case #{t + 1}: {ans}")
