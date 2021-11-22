# Rock Paper Scissors
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435c44/00000000007ec28e
# Use DP to find best strategy
# dp[r][p][s]: the max expected value when making r rocks and p papers and s scissors on N-th day
# r + p + s = N
# dp[r][p][s] = max(choose rock on the last day, choose paper, choose scissor)
# = max((dp[r-1][p][s] + p / (n - 1) * W + s / (n - 1) * E),    # opponent has p / (n - 1) to choose scissor, so I win; s / (n - 1) to choose rock, so tie
#       (dp[r][p-1][s] + s / (n - 1) * W + r / (n - 1) * E),
#       (dp[r][p][s-1] + r / (n - 1) * W + p / (n - 1) * E))
# dp[1][0][0] = dp[0][1][0] = dp[0][0][1] = 1/3 * W + 1/3 * E
# O(N^3) to fill the table

N = 60
T = int(input())
X = int(input())
for t in range(T):
    [W, E] = [int(n) for n in input().split()]
    dp = [[[0] * (N + 1) for j in range(N + 1)] for i in range(N + 1)]
    choice = [[[""] * (N + 1) for j in range(N + 1)] for i in range(N + 1)]

    dp[1][0][0] = 1/3 * W + 1/3 * E
    dp[0][1][0] = 1/3 * W + 1/3 * E
    dp[0][0][1] = 1/3 * W + 1/3 * E
    choice[1][0][0] = "R"
    choice[0][1][0] = "P"
    choice[0][0][1] = "S"

    for n in range(2, 61):
        for r in range(0, n + 1):
            for p in range(0, n + 1 - r):
                s = n - r - p
                # print(n, r, p, s)
                choose_r = (dp[r-1][p][s] + p / (n - 1) * W + s / (n - 1) * E) if r != 0 else 0
                choose_p = (dp[r][p-1][s] + s / (n - 1) * W + r / (n - 1) * E) if p != 0 else 0
                choose_s = (dp[r][p][s-1] + r / (n - 1) * W + p / (n - 1) * E) if s != 0 else 0
                dp[r][p][s] = max(choose_r, choose_p, choose_s)
                if dp[r][p][s] == choose_r:
                    choice[r][p][s] = choice[r-1][p][s] + "R"
                elif dp[r][p][s] == choose_p:
                    choice[r][p][s] = choice[r][p-1][s] + "P"
                else:
                    choice[r][p][s] = choice[r][p][s-1] + "S"

    result = ""
    max_point = 0
    for r in range(0, N + 1):
        for p in range(0, N + 1 - r):
            s = N - r - p
            if dp[r][p][s] > max_point:
                max_point = dp[r][p][s]
                result = choice[r][p][s]

    print(f"Case #{t + 1}: {result}")
