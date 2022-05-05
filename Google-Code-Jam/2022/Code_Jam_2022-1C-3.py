# Intranets
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000877b42/0000000000afdf76
# O(N^4), MLE on test set 2

MOD = pow(10, 9) + 7
def modInverse(a, m):
    ans = 1
    while m:
        if m & 1:
            ans = ans * a % MOD
        m >>= 1
        a = a * a % MOD
    return ans

# MAX_N = 500000
MAX_N = 50
fac = [1] * (MAX_N * MAX_N + 1)
rfac = [1] * (MAX_N * MAX_N + 1)
for i in range(1, MAX_N * MAX_N + 1):
    fac[i] = fac[i - 1] * i % MOD
rfac[MAX_N * MAX_N] = modInverse(fac[MAX_N * MAX_N], MOD - 2)
for i in range(MAX_N * MAX_N - 1, 0, -1):
    rfac[i] = rfac[i + 1] * (i + 1) % MOD

def C(n, k):
    if n < k:
        return 0
    else:
        return fac[n] * rfac[k] * rfac[n - k]

T = int(input())
for t in range(T):
    [N, K] = [int(x) for x in input().split()]

    total = N * (N - 1) // 2
    curr = [[0] * (N+1) for _ in range(N+1)]
    # curr[j][k]: The # of permutations that first i edges have j nodes and form k intranets
    curr[0][0] = 1
    
    # Assign one edge at a time
    for i in range(1, total + 1):
        next = [[0] * (N+1) for _ in range(N+1)]
        for j in range(2, N+1):
            for k in range(1, N+1):
                # Let the current edge be (u, v), S_i be the node set connected by first i edges, there can be 3 cases
                # u ∈ Si, v ∈ Si, edge not activated, node size and intranet size not changed
                next[j][k] += max(0, C(j, 2) - (i - 1)) * curr[j][k]
                # u ∉ Si, v ∉ Si, node size += 2, intranet size += 1
                next[j][k] += C(N - (j - 2), 2) * curr[j - 2][k - 1]
                # u ∈ Si, v ∉ Si, node size += 1, intranet size not changed
                next[j][k] += (N - (j - 1)) * (j - 1) * curr[j - 1][k]
                next[j][k] %= MOD
        curr = next

    ans = curr[N][K] * rfac[total] % MOD
    print(f"Case #{t + 1}: {ans}")
