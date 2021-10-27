# Wandering Robot
# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ffc8/00000000002d8565
# O(W*H), MLE on test set 2

T = int(input())
for t in range(T):
    [W, H, L, U, R, D] = [int(n) for n in input().split()]

    prob = [[0] * (W+1) for i in range(H+1)]
    prob[1][1] = 1
    for level in range(3, max(R + U, L + D) + 1):
        for i in range(max(1, level - W), min(level, H + 1)):
        # for x in range(max(1, i-H), min(i, W+1)):
            j = level - i
            # print(i, j)
            temp = 0
            if j < L or j > R or i - 1 < U or i - 1 > D:
                if j == W: # [i - 1][W] can only go down
                    temp += prob[i - 1][j]
                else:
                    temp += prob[i - 1][j] / 2
            if i < U or i > D or j - 1 < L or j - 1 > R:
                if i == H: # [H][j - 1] can only go right
                    temp += prob[i][j - 1]
                else:
                    temp += prob[i][j - 1] / 2
            prob[i][j] = temp
    # for i in range(H+1):
    #     print(prob[i])

    ans = 0
    for i in range(L, R+1):
        ans += prob[U][i]
    for i in range(U+1, D+1):
        ans += prob[i][L]
    ans = 1 - ans

    print(f"Case #{t + 1}: {ans}")
