# Controlled Inflation
# https://codingcompetitions.withgoogle.com/codejam/round/000000000087711b/0000000000accfdb
# Key idea: it's always optimal for a customer to have all increasing / decreasing product
# DP, O(2N)

T = int(input())
for t in range(T):
    [N, P] = [int(x) for x in input().split()]
    min_p = []
    max_p = []
    for _ in range(N):
        temp = [int(x) for x in input().split()]
        min_p.append(min(temp))
        max_p.append(max(temp))

    dp = [[0] * 2 for _ in range(N+1)]
    # dp[i][0]: the min # of operations of first i customers, and the product of customer i are increasing; dp[i][1] for decreasing
    start0 = 0 # If previous customer ends with increasing
    start1 = 0 # If previous customer ends with decreasing
    for i in range(N):
        dp[i+1][0] = min(dp[i][0] + abs(start0 - min_p[i]), dp[i][1] + abs(start1 - min_p[i])) + (max_p[i] - min_p[i])
        dp[i+1][1] = min(dp[i][0] + abs(start0 - max_p[i]), dp[i][1] + abs(start1 - max_p[i])) + (max_p[i] - min_p[i])
        start0 = max_p[i]
        start1 = min_p[i]

    ans = min(dp[N][0], dp[N][1])
    print(f"Case #{t + 1}: {ans}")
