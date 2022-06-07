# Palindromic Deletions
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000008cb4d1/0000000000b20d16
# Brute-force, O(N!), TLE on test set 2

MOD = pow(10, 9) + 7

def my_pow(a, b):
    ans = 1
    while b:
        if b & 1:
            ans = ans * a % MOD
        b >>= 1
        a = a * a % MOD
    return ans

def is_palindrome(S):
    N = len(S)
    for i in range(N // 2):
        if S[i] != S[N - 1 - i]:
            return False
    return True

def solve(S):
    N = len(S)
    if N == 1:
        return 2
    else:
        ans = int(is_palindrome(S)) * fac[N]
        for i in range(N):
            new_S = S[0:i] + S[i+1:]
            ans += solve(new_S)
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

    ans = solve(S) - int(is_palindrome(S)) * fac[N]
    ans = ans * rfac[N] % MOD

    print(f"Case #{t + 1}: {ans}")
