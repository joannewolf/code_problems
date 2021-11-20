# Training
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050e01/00000000000698d6

INF = pow(10, 10)
T = int(input())
for t in range(T):
    [N, P] = [int(n) for n in input().split()]
    skills = [int(n) for n in input().split()]
    skills.sort()

    prefix_sum = [0]
    for i in range(N):
        prefix_sum.append(prefix_sum[-1] + skills[i])

    ans = INF
    for i in range(N - P + 1):
        ans = min(ans, P * skills[i + P - 1] - (prefix_sum[i + P] - prefix_sum[i]))

    print(f"Case #{t + 1}: {ans}")
