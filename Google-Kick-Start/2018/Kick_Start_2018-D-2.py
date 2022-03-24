# Paragliding
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050ee1/0000000000051006
# O(NK), TLE on test set 2

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

    ans = 0
    # For i-th balloon, iterate each tower to see if the height is enough to pass it
    for i in range(K):
        for j in range(N):
            if H[j] >= abs(X[i] - P[j]) + Y[i]:
                ans += 1
                break

    print(f"Case #{t + 1}: {ans}")
