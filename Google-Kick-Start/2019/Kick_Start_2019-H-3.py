# Elevanagram
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050edd/00000000001a286d

T = int(input())
for t in range(T):
    nums = [int(x) for x in input().split()]

    count_10 = 0 # Number of A_i which >= 10
    index_10 = [] # Which digit having number >= 10
    for i in range(9):
        if nums[i] >= 10:
            count_10 += 1
            index_10.append(i)

    # When there are at least 2 digits having count >= 10, say it's digit i and j
    # First we can randomly group all the digits into two halves, A and B, r = (A - B) % 11 could be 0 ~ 10
    # However, by exchanging (i, j) k times, k = 0 ~ 10, r' = (A - B) - 2k(i - j)
    # We can always find a k to make r' = 0, cuz for k = 0 ~ 10, 2k(i - j) % 11 could be also 0 ~ 10, and we can choose the remain value we need to make r' = 0
    if count_10 >= 2:
        ans = "YES"
    else:
        # When there's only one digit having count >= 10 and if it's large enough, the range for j will not be 0 ~ A_i
        # For example, Ai = 1000 and all other Aj = 9, total 1072 numbers, then two halves must be (536, 536)
        # Even we put all other 72 numbers on one side, there must be at least (536-72)=464 digit i on the same side
        # -> there could be (536-72)=464 ~ 536 digit i on one side -> simplify it to be (464-464)=0 ~ (536-464)=72 -> there could be 0 ~ 72 digit i on one side
        # While sum(A) is odd number, for example Ai = 999 and all other Aj = 9, total 1071 numbers, two halves could be (535, 536) or (536, 535)
        # -> there could be (535-72)=463 ~ 536 digit i on one side -> simplify it to be (463-463)=0 ~ (536-463)=73 -> there could be 0 ~ 73 digit i on one side
        # After simplifying, all Ai are small enough to use dp to solve
        if count_10 == 1 and nums[index_10[0]] >= sum(nums) - nums[index_10[0]]:
            nums[index_10[0]] = (sum(nums) - nums[index_10[0]]) + sum(nums) % 2
        nums.insert(0, 0)
        N = sum(nums)
        current_count = 0
        dp = [[[False] * 11 for _ in range(N+1)] for _ in range(10)]
        # dp[i][j][k]: Whether it's possible using digits 1 ~ i, with current # of digits in positive side = j, such that current sum % 11 = k
        dp[0][0][0] = True
        for i in range(1, 10):
            for start in range(current_count + 1): # There's "start" digits in positive side currently
                for j in range(nums[i] + 1): # For current digit i, put j out of A_i in positive side, and (nums[i] - j) in negative side
                    for k in range(11):
                        dp[i][start + j][(k + (j - (nums[i] - j)) * i) % 11] |= dp[i - 1][start][k]
            # print(dp[i])
            current_count += nums[i]

        if dp[9][N // 2][0]:
            ans = "YES"
        else:
            ans = "NO"

    print(f"Case #{t + 1}: {ans}")
