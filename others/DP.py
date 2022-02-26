# https://en.wikipedia.org/wiki/Knapsack_problem
# Given a set of items, each with a weight and a value
# Determine the number of each item to include in a collection so that the sum(weight) <= K and maximize sum(value)

# 0-1 knapsack problem, either take or not take the item, weight > 0
# O(NW)
def knapsack_0_1(W, N):
    # dp[i][w]: the max value <= w using first i items
    dp = [[0] * (W + 1) for i in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(1, W + 1):
            if w[i] > j:
                dp[i][j] = dp[i - 1][j] # Never take item i
            else:
                option1 = dp[i - 1][j - w[i]] + v[i] # Take item i
                option2 = dp[i - 1][j] # Not take item i
                dp[i][j] = max(option1, option2)
    ans = dp[N][W]