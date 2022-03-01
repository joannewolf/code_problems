# Shifts
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050e02/000000000018fd0d
# O((2^N)^2), TLE on test set 2

T = int(input())
for t in range(T):
    [N, H] = [int(x) for x in input().split()]
    A = [int(x) for x in input().split()]
    B = [int(x) for x in input().split()]

    # Get all combinations of shifts which make them happy
    M = pow(2, N)
    comb_A = set()
    comb_B = set()
    for combination in range(M):
        num = combination
        temp_A = 0
        temp_B = 0
        for i in range(N):
            if num % 2 == 1:
                temp_A += A[i]
                temp_B += B[i]
            num //= 2
        if temp_A >= H:
            comb_A.add(combination)
        if temp_B >= H:
            comb_B.add(combination)

    ans = 0
    for c1 in comb_A:
        for c2 in comb_B:
            # Check if A and B can cover all shifts
            if c1 | c2 == M - 1:
                ans += 1

    print(f"Case #{t + 1}: {ans}")
