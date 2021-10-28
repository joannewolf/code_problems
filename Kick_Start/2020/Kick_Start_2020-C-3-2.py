# Perfect Subarray
# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff43/00000000003381cb
# O(N * sqrt(N * MAX_A))

import math

T = int(input())
for t in range(T):
    N = int(input())
    num = [int(n) for n in input().split()]

    square = []
    if max(num) >= 0:
        for i in range(int(math.sqrt(max(num) * N)) + 1):
            square.append(i * i)
    # print(square)

    ans = [0] * N # ans[i]: the number of subarrays which end at num[i] and sum is square num
    prefix_sum = {} # prefix_sum[key]: the number of indices i such that sum(A[0...i])=key
    prefix_sum[0] = 1
    current_sum = 0
    for i in range(N):
        current_sum += num[i]
        for s in square:
            if current_sum - s in prefix_sum:
                # Because sum of subarray = current_sum A[0...i] - prefix_sum A[0...j]
                ans[i] += prefix_sum[current_sum - s]
        if current_sum in prefix_sum:
            prefix_sum[current_sum] += 1
        else:
            prefix_sum[current_sum] = 1

    print(f"Case #{t + 1}: {sum(ans)}")
