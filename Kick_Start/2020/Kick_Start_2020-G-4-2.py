# Merge Cards
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000001a0069/0000000000415054
# Optimize the DP solution, O(N^2)

T = int(input())
for t in range(T):
    N = int(input())
    nums = [int(n) for n in input().split()]

    num_sum = [0] # i < j, nums[i] ~ nums[j] = num_sum[j + 1] - num_sum[i]
    for i in range(N):
        num_sum.append(num_sum[-1] + nums[i])
    # dp[i][j]: the expected value to construct nums[i]~nums[j], inclusive
    prefix_sum = [0.0] * N # prefix_sum[i]: sum(dp[i][i] ~ dp[i][current])
    suffix_sum = [0.0] * N # suffix_sum[i]: sum(dp[i][current] ~ dp[i][i])

    for i in range(1, N):
        for start in range(N - i):
            # Calculate dp[start][start + i]
            temp_sum = (prefix_sum[start] + suffix_sum[start + i]) / i + (num_sum[start + i + 1] - num_sum[start])
            ans = temp_sum
            prefix_sum[start] += temp_sum
            suffix_sum[start + i] += temp_sum

    print(f"Case #{t + 1}: {ans}")
