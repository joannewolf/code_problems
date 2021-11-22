# Mural
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000051060/0000000000058b89

T = int(input())
for t in range(T):
    N = int(input())
    scores = [int(c) for c in input()]

    prefix_sum = [0]
    for i in range(N):
        prefix_sum.append(prefix_sum[-1] + scores[i])

    num = (N + 1) // 2
    ans = 0
    for i in range(num, N + 1):
        ans = max(ans, prefix_sum[i] - prefix_sum[i - num])

    print(f"Case #{t + 1}: {ans}")
