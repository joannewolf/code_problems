# Product Triplets
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000051066/0000000000051187
# O(N^2)

T = int(input())
for t in range(T):
    N = int(input())
    nums = [int(x) for x in input().split()]

    num_count = {}
    for x in nums:
        if x not in num_count:
            num_count[x] = 1
        else:
            num_count[x] += 1

    ans = 0
    if 0 in num_count: # 0 times anything equals 0
        zeros = num_count.pop(0)
        ans += zeros * (zeros - 1) * (zeros - 2) // 6 # (0, 0, 0)
        ans += zeros * (zeros - 1) // 2 * (N - zeros) # (0, 0, x)
    if 1 in num_count: # 1 times anything equals to themselves
        ones = num_count.pop(1)
        ans += ones * (ones - 1) * (ones - 2) // 6 # (1, 1, 1)
        for (k, v) in num_count.items():
            if v >= 2:
                ans += ones * v * (v - 1) // 2 # (1, x, x)

    N = len(num_count)
    nums = list(num_count.keys()) # Distinct remaining numbers
    for i in range(N):
        x = num_count[nums[i]]
        if x >= 2 and nums[i] * nums[i] in num_count: # (x, x, y)
            y = num_count[nums[i] * nums[i]]
            ans += x * (x - 1) // 2 * y
        for j in range(i+1, N):
            if nums[i] * nums[j] in num_count: # (x, y, z)
                y = num_count[nums[j]]
                z = num_count[nums[i] * nums[j]]
                ans += x * y * z

    print(f"Case #{t + 1}: {ans}")
