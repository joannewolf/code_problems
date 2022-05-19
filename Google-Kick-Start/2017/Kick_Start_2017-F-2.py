# Kicksort
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000201d29/0000000000201b7c

T = int(input())
for t in range(T):
    N = int(input())
    nums = [int(x) for x in input().split()]

    flag_min = 1
    flag_max = N
    for size in range(N, 0, -1):
        pivot = (size - 1) // 2
        # print(size, nums, pivot)
        if nums[pivot] == flag_min:
            flag_min += 1
            nums.pop(pivot)
        elif nums[pivot] == flag_max:
            flag_max -= 1
            nums.pop(pivot)
        else:
            break

    if nums:
        print(f"Case #{t + 1}: NO")
    else:
        print(f"Case #{t + 1}: YES")
