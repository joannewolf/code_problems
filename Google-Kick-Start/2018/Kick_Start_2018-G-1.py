# Product Triplets
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000051066/0000000000051187
# Brute-force, O(N^3), TLE on test set 2

T = int(input())
for t in range(T):
    N = int(input())
    nums = [int(x) for x in input().split()]

    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if nums[i] * nums[j] == nums[k] or nums[i] * nums[k] == nums[j] or nums[j] * nums[k] == nums[i]:
                    ans += 1

    print(f"Case #{t + 1}: {ans}")
