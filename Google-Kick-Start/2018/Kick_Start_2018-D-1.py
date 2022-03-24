# Candies
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050ee1/00000000000510ef
# O(N^2), TLE on test set 1

N_INF = -pow(10, 15) - 1

T = int(input())
for t in range(T):
    [N, O, D] = [int(x) for x in input().split()]
    [X1, X2, A, B, C, M, L] = [int(x) for x in input().split()]
    S = [X1, X2]
    for i in range(2, N):
        next = (S[-1] * A + S[-2] * B + C) % M
        S.append(next)
    for i in range(N):
        S[i] += L
    # print(S)

    odd = [0]
    sum = [0]
    for i in range(N):
        sum.append(sum[-1] + S[i])
        odd.append(odd[-1] + (S[i] % 2))
    # print(sum)
    # print(odd)

    ans = N_INF
    for l in range(1, N+1):
        for r in range(l, N+1):
            if odd[r] - odd[l-1] <= O and sum[r] - sum[l-1] <= D and sum[r] - sum[l-1] > ans:
                ans = sum[r] - sum[l-1]

    if ans == N_INF:
        print(f"Case #{t + 1}: IMPOSSIBLE")
    else:
        print(f"Case #{t + 1}: {ans}")
