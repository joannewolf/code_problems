# Palindromic Deletions
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000008cb4d1/0000000000b20d16
# Key idea: any panlindrome will be a subsequence of the input string S
# For a palindrome of length K, the # of games we will encounter it is (N - K)! * K!, first removing the unused char, then remove the used K char
# let f(K) = # of palindrome subsequence with len K, numerator = SUM{f(K) * (N - K)! * K!}, K = 0~N-1
# To find f(K), use DP
# O(N^3)

MOD = pow(10, 9) + 7

def my_pow(a, b):
    ans = 1
    while b:
        if b & 1:
            ans = ans * a % MOD
        b >>= 1
        a = a * a % MOD
    return ans

MAX_N = 400
fac = [1] * (MAX_N + 1)
rfac = [1] * (MAX_N + 1)
for i in range(1, MAX_N + 1):
    fac[i] = fac[i - 1] * i % MOD
rfac[MAX_N] = my_pow(fac[MAX_N], MOD - 2)
for i in range(MAX_N - 1, 0, -1):
    rfac[i] = rfac[i + 1] * (i + 1) % MOD

T = int(input())
for t in range(T):
    N = int(input())
    S = input()

    dp = [[[0] * N for _ in range(N)] for _ in range(N)]
    # dp[l][r][k]: in substr S[l, r], inclusive, the # of palindrome subsequence of len k
    for l in range(N):
        for r in range(N):
            dp[l][r][0] = 1

    for k in range(1, N):
        for gap in range(k, N+1):
            for l in range(N - gap + 1):
                r = l + gap - 1
                if l == r:
                    dp[l][r][k] = 1
                else:
                    dp[l][r][k] = dp[l][r-1][k] + dp[l+1][r][k] - dp[l+1][r-1][k]
                    if r > l and S[l] == S[r]:
                        dp[l][r][k] += dp[l+1][r-1][k-2]
                dp[l][r][k] %= MOD
    # for k in range(N):
    #     print("k", k)
    #     for l in range(N):
    #         row = [dp[l][r][k] for r in range(N)]
    #         print(row)

    ans = 0
    for k in range(N):
        ans += dp[0][N - 1][k] * fac[k] * fac[N - k] % MOD
    ans = ans * rfac[N] % MOD

    print(f"Case #{t + 1}: {ans}")
