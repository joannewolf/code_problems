# Maximum Gain
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000008caea6/0000000000b76fae

MAX_INT = pow(10, 14)

T = int(input())
for t in range(T):
    N = int(input())
    A = [int(x) for x in input().split()]
    M = int(input())
    B = [int(x) for x in input().split()]
    K = int(input())

    # Find min subarray sum in A and B, and the two subarray length sum be (N + M - K)
    K2 = N + M - K
    prefix_A = [0]
    prefix_B = [0]
    for i in range(N):
        prefix_A.append(prefix_A[-1] + A[i])
    for i in range(M):
        prefix_B.append(prefix_B[-1] + B[i])
    # print(prefix_A)
    # print(prefix_B)

    ans = MAX_INT
    for i in range(max(0, K2 - M), min(N, K2) + 1):
        # Use subarray len i in A, and subarray len j in B, find the min subarray value respectively
        j = K2 - i
        min_A = MAX_INT
        min_B = MAX_INT
        for l in range(N - i + 1):
            r = l + i
            min_A = min(min_A, prefix_A[r] - prefix_A[l])
        for l in range(M - j + 1):
            r = l + j
            min_B = min(min_B, prefix_B[r] - prefix_B[l])

        if i == 0:
            min_A = 0
        if j == 0:
            min_B = 0

        ans = min(ans, min_A + min_B)

    ans = sum(A) + sum(B) - ans

    print(f"Case #{t + 1}: {ans}")
