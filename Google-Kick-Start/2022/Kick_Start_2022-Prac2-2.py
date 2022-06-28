# Sherlock and Parentheses
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000008f4a94/0000000000b5496b

T = int(input())
for t in range(T):
    [L, R] = [int(x) for x in input().split()]

    base = min(L, R)
    ans = (1 + base) * base // 2
    print(f"Case #{t + 1}: {ans}")
