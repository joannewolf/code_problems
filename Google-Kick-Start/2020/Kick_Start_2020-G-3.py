# Combination Lock
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000001a0069/0000000000414a24
# O(W^2), TLE on test set 3

INF = pow(10, 14)
T = int(input())
for t in range(T):
    [W, N] = [int(n) for n in input().split()]
    nums = [int(n) for n in input().split()]

    ans = INF
    for x in nums:
        sum = 0
        for y in nums:
            diff = abs(x - y)
            sum += min(diff, N - diff)
        ans = min(ans, sum)

    print(f"Case #{t + 1}: {ans}")
