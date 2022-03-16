# Sherlock and the Bit Strings
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050ff4/000000000005107b
# Only pass small data set, where A = B, after we fix the K required bits, we just use P-1's bits to fill the rest spaces

T = int(input())
for t in range(T):
    [N, K, P] = [int(x) for x in input().split()]
    limits = []
    for _ in range(K):
        [a, b, c] = [int(x) for x in input().split()]
        limits.append((a, b, c))

    ans = [-1] * N
    for (a, b, c) in limits:
        ans[a - 1] = c
    P -= 1
    flag = N - 1
    for i in range(N - K):
        while ans[flag] != -1:
            flag -= 1
        ans[flag] = P % 2
        P //= 2

    print(f"Case #{t + 1}: {''.join(map(str, ans))}")
