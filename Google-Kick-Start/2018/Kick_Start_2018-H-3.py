# Let Me Count The Ways
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050ee2/0000000000051189
# Permutation having pair together = (Having 1 pair together) - (2 pair together) + (3 pair together) ...
# (2N)! - SUM{(-1)^(i+1) * C(M, i) * (2N - i)! * 2^i}, i = 1~M
# = SUM{(-1)^i * C(M, i) * (2N - i)! * 2^i}, i = 0~M
# RE but correct locally on test set 1, math.comb only available after python 3.8

from math import comb

MOD = pow(10, 9) + 7
frac = [1]

for i in range(1, 201):
    frac.append(frac[-1] * i)
# print(frac[200])

T = int(input())
for t in range(T):
    [N, M] = [int(x) for x in input().split()]

    ans = 0
    for i in range(M+1):
        ans += pow(-1, i) * comb(M, i) * frac[2 * N - i] * pow(2, i)

    print(f"Case #{t + 1}: {ans % MOD}")
