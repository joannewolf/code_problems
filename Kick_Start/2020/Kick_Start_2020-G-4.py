# Merge Cards
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000001a0069/0000000000415054
# DP, O(N^3), TLE on test set 3

T = int(input())
for t in range(T):
    N = int(input())
    nums = [int(n) for n in input().split()]
    dp = [[0] * N for i in range(N)] # dp[i][j]: the expected value to construct nums[i]~nums[j], inclusive

    for i in range(1, N):
        for start in range(N - i):
            temp_sum = 0
            for cut in range(start, start + i):
                temp_sum += dp[start][cut] + dp[cut + 1][start + i]
            # Each cut has equal probability to occur, so just need to divide sum by i
            # And last round merge will always add sum of subarray
            temp_sum = temp_sum / i + sum(nums[start: start + i + 1])
            dp[start][start + i] = temp_sum

    print(f"Case #{t + 1}: {dp[0][N - 1]}")
