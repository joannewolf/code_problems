# Sample Problem
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000008f4332/0000000000942404

T = int(input())
for t in range(T):
    [N, M] = [int(n) for n in input().split()]
    C = [int(n) for n in input().split()]

    ans = sum(C) % M
    print(f"Case #{t + 1}: {ans}")
