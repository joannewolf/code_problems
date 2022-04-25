# Pancake Deque
# https://codingcompetitions.withgoogle.com/codejam/round/000000000087711b/0000000000acd59d

T = int(input())
for t in range(T):
    N = int(input())
    nums = [int(x) for x in input().split()]

    ans = 0
    now = -1
    left, right = 0, N - 1
    while left <= right:
        # print("left", left, "right", right)
        if nums[left] < nums[right]:
            if nums[left] >= now:
                now = nums[left]
                ans += 1
            left += 1
        else:
            if nums[right] >= now:
                now = nums[right]
                ans += 1
            right -= 1

    print(f"Case #{t + 1}: {ans}")
