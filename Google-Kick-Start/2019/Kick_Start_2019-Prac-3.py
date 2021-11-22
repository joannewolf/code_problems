# Kickstart Alarm
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000051060/0000000000058a56
# Brute-force, O(K*N^3), TLE on test set 2

MOD = pow(10, 9) + 7
T = int(input())
for t in range(T):
    [N, K, x0, y0, C, D, Ex, Ey, F] = [int(n) for n in input().split()]
    A = [(x0 + y0) % F]
    for i in range(1, N):
        A.append((A[-1] * (C + D) + Ex + Ey) % F)
    # print(A)

    ans = 0
    for i in range(1, K + 1):
        for len in range(N):
            for start in range(N - len):
                for j in range(start, start + len + 1):
                    ans += A[j] * pow(j - start + 1, i)
        ans %= MOD

    print(f"Case #{t + 1}: {ans}")
