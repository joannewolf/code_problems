# Controlled Inflation
# https://codingcompetitions.withgoogle.com/codejam/round/000000000087711b/0000000000accfdb
# Key idea: it's always optimal for a customer to have all increasing / decreasing product
# Brute-force, O(2^N), TLE on test set 2

def solve(i, start):
    if i == N:
        return 0
    option1 = abs(min_p[i] - start) + (max_p[i] - min_p[i]) + solve(i + 1, max_p[i])
    option2 = abs(max_p[i] - start) + (max_p[i] - min_p[i]) + solve(i + 1, min_p[i])
    return min(option1, option2)

T = int(input())
for t in range(T):
    [N, P] = [int(x) for x in input().split()]
    min_p = []
    max_p = []
    for _ in range(N):
        temp = [int(x) for x in input().split()]
        min_p.append(min(temp))
        max_p.append(max(temp))

    print(f"Case #{t + 1}: {solve(0, 0)}")
