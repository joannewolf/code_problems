# Reversort
# https://codingcompetitions.withgoogle.com/codejam/round/000000000043580a/00000000006d0a5c

T = input()
for t in range(int(T)):
    N = int(input())
    nums = [int(n) for n in input().split()]

    result = 0
    for i in range(N - 1):
        j = nums.index(min(nums[i:]))
        # print(nums, j)
        result += (j - i + 1)
        nums[i : j + 1] = nums[i : j + 1][::-1]

    print("Case #{}: {}".format(t + 1, result))
