# Candies
# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff43/0000000000337b4d
# O(1) on query, O(N) on update, TLE on test set 2

T = int(input())
for t in range(T):
    [N, Q] = [int(n) for n in input().split()]
    num = [int(n) for n in input().split()]

    # If using segment tree, can achieve O(logN) on query, O(logN) on update
    sum = [0]
    ladder_sum = [0]
    for i in range(N):
        sum.append(sum[-1] + pow(-1, i) * num[i])
        ladder_sum.append(ladder_sum[-1] + pow(-1, i) * (i + 1) * num[i])

    ans = 0
    for i in range(Q):
        [type, x, y] = input().split()
        x = int(x)
        y = int(y)
        if type == 'U':
            for j in range(x, N + 1):
                sum[j] = sum[j] - pow(-1, x - 1) * num[x - 1] + pow(-1, x - 1) * y
                ladder_sum[j] = ladder_sum[j] - (pow(-1, x - 1) * x * num[x - 1]) + (pow(-1, x - 1) * x * y)
            num[x - 1] = y
        else:
            ans += pow(-1, x - 1) * (ladder_sum[y] - ladder_sum[x - 1] - (x - 1) * (sum[y] - sum[x - 1]))

    print(f"Case #{t + 1}: {ans}")
