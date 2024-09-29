# Image Labeler
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000008caea6/0000000000b76e11
# M - 1 largest nums assign to category on their own, and the rest assigned to the last category

T = int(input())
for t in range(T):
    [N, M] = [int(x) for x in input().split()]
    nums = [int(x) for x in input().split()]
    nums.sort()

    flag = N - (M - 1)
    ans = sum(nums[flag:])
    if flag % 2 == 1:
        ans += nums[flag // 2]
    else:
        ans += (nums[flag // 2 - 1] + nums[flag // 2]) / 2

    print(f"Case #{t + 1}: {ans}")
