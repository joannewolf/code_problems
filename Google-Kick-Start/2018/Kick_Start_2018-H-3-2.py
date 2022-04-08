# Let Me Count The Ways
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050ee2/0000000000051189
# Permutation having pair together = (Having 1 pair together) - (2 pair together) + (3 pair together) ...
# (2N)! - SUM{(-1)^(i+1) * C(M, i) * (2N - i)! * 2^i}, i = 1~M
# = SUM{(-1)^i * C(M, i) * (2N - i)! * 2^i}, i = 0~M

MOD = pow(10, 9) + 7
fact = [1]
pow2 = [1]
invfact = [1]
MAX_N = 200010

def modInverse(a, m):
    m0 = m
    y = 0
    x = 1
 
    if (m == 1):
        return 0
 
    while (a > 1):
        q = a // m # quotient
        t = m

        # m is remainder now, process, same as Euclid's algo
        m = a % m
        a = t
        t = y
 
        # Update x and y
        y = x - q * y
        x = t

    # Make x positive
    if (x < 0):
        x = x + m0

    return x

for i in range(1, MAX_N):
    fact.append(fact[-1] * i % MOD)
    pow2.append(pow2[-1] * 2 % MOD)
    invfact.append(modInverse(fact[-1], MOD))

T = int(input())
for t in range(T):
    [N, M] = [int(x) for x in input().split()]

    ans = 0
    for i in range(M+1):
        ans += pow(-1, i) * fact[M] * invfact[i] * invfact[M - i] * fact[2 * N - i] * pow2[i] % MOD

    print(f"Case #{t + 1}: {ans % MOD}")
