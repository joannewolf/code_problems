# Unlock the Padlock
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000008caa74/0000000000acef55

def rotate(start: int, end: int):
    return min(abs(end - start), D - abs(end - start))

T = int(input())
for t in range(T):
    [N, D] = [int(x) for x in input().split()]
    raw = [int(x) for x in input().split()] + [-1]

    # Neighbor same nums can be processed together, get distinct nums first
    flag = raw[0]
    nums = []
    for v in raw:
        if v != flag:
            nums.append(flag)
            flag = v
    # print(nums)

    N = len(nums)
    dp = [[[-1] * 2 for _ in range(N)] for _ in range(N)]
    # dp[i][j][0]: The min move to unlock padlock i~j, inclusive, and end with nums[i]; dp[i][j][1]: end with nums[j]
    for i in range(N):
        dp[i][i][0] = dp[i][i][1] = 0
    
    for gap in range(1, N):
        for l in range(N - gap):
            r = l + gap
            dp[l][r][0] = min(dp[l+1][r][0] + rotate(nums[l+1], nums[l]), dp[l+1][r][1] + rotate(nums[r], nums[l]))
            dp[l][r][1] = min(dp[l][r-1][0] + rotate(nums[l], nums[r]), dp[l][r-1][1] + rotate(nums[r-1], nums[r]))

    ans = min(dp[0][N-1][0] + rotate(nums[0], 0), dp[0][N-1][1] + rotate(nums[N-1], 0))
    print(f"Case #{t + 1}: {ans}")
