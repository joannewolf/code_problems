# Banana Bunches
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000004362d6/00000000008b44ef
# The problem can be translate to finding 2 non-overlapping interval (i, j), (x, y) and i <= j < x <= y
# Such that sum(B[i:j+1]) + sum(B[x:y+1]) = K and j - i + 1 + y - x + 1 is minimum
# Store the optimal length of second subarray for each sum, then iterate all pair of (i, j)
# O(N^2)

MAX_INT = pow(10, 7)

T = int(input())
for t in range(T):
    [N, K] = [int(n) for n in input().split()]
    B = [int(n) for n in input().split()]

    if K in B:
        print(f"Case #{t + 1}: 1")
        continue

    result = MAX_INT
    best = [MAX_INT] * (K + 1)
    for j in range(N - 1, -1, -1):
        temp_sum = 0 # sum of B[i] ~ B[j]
        for i in range(j, -1, -1):
            temp_sum += B[i]
            if temp_sum <= K:
                result = min(result, j - i + 1 + best[K - temp_sum])
        
        # Grow second subarray from small to big
        temp_sum_2 = 0 # sum of B[j] ~ B[x]
        for x in range(j, N):
            temp_sum_2 += B[x]
            if temp_sum_2 <= K:
                best[temp_sum_2] = min(best[temp_sum_2], x - j + 1)

    if result == MAX_INT:
        print(f"Case #{t + 1}: -1")
    else:
        print(f"Case #{t + 1}: {result}")
