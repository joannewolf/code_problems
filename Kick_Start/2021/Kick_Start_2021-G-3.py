# Banana Bunches
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000004362d6/00000000008b44ef
# The problem can be translate to finding 2 non-overlapping interval (i, j), (x, y) and i <= j < x <= y
# Such that sum(B[i:j+1]) + sum(B[x:y+1]) = K and j - i + 1 + y - x + 1 is minimum
# For all pairs of (j, x) use two pointer to find optimal y for each i
# O(N^2 * N) = O(N^3), TLE on test set 2

MAX_INT = pow(10, 7)

T = int(input())
for t in range(T):
    [N, K] = [int(n) for n in input().split()]
    B = [int(n) for n in input().split()]

    if K in B:
        print(f"Case #{t + 1}: 1")
        continue

    pre_sum = []
    # pre_sum[i]: sum of B[0] ~ B[i]
    temp_sum = 0
    for i in range(N):
        temp_sum += B[i]
        pre_sum.append(temp_sum)

    result = MAX_INT
    for j in range(N):
        for x in range(j + 1, N):
            i = 0
            y = x
            while i <= j and y < N:
                temp_sum = (pre_sum[j] - pre_sum[i] + B[i]) + (pre_sum[y] - pre_sum[x] + B[x])
                if temp_sum == K:
                    # print(i, j, x, y)
                    result = min(result, j - i + 1 + y - x + 1)
                    i += 1
                elif temp_sum < K:
                    y += 1
                else:
                    i += 1

    if result == MAX_INT:
        print(f"Case #{t + 1}: -1")
    else:
        print(f"Case #{t + 1}: {result}")
