# Intranets
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000877b42/0000000000afdf76
# From toxicpie and KoD's answer, need explanation

MOD = pow(10, 9) + 7
def my_pow(a, m):
    ans = 1
    while m:
        if m & 1:
            ans = ans * a % MOD
        m >>= 1
        a = a * a % MOD
    return ans

MAX_N = 500000
fac = [1] * (2 * MAX_N + 1)
rfac = [1] * (2 * MAX_N + 1)
inv = [1] * (2 * MAX_N + 1)
for i in range(1, 2 * MAX_N + 1):
    fac[i] = fac[i - 1] * i % MOD
rfac[2 * MAX_N] = my_pow(fac[2 * MAX_N], MOD - 2)
for i in range(2 * MAX_N - 1, 0, -1):
    rfac[i] = rfac[i + 1] * (i + 1) % MOD
for i in range(1, 2 * MAX_N + 1):
    inv[i] = rfac[i] * fac[i - 1] % MOD

def C(n, k):
    if n < k:
        return 0
    else:
        return fac[n] * rfac[k] * rfac[n - k] % MOD

T = int(input())
for t in range(T):
    [N, K] = [int(x) for x in input().split()]

    N -= 1
    K -= 1
    p = my_pow(2, N - 2 * K - 1) * C(N - 1, 2 * K) * C(2 * K, K) * inv[K + 1] % MOD
    q = C(2 * N, N) * inv[N + 1] % MOD
    inv_q = my_pow(q, MOD - 2)

    print(f"Case #{t + 1}: {p * inv_q % MOD}")
