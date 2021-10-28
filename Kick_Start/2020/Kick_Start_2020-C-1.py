# Countdown
# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff43/00000000003380d2

T = int(input())
for t in range(T):
    [N, K] = [int(n) for n in input().split()]
    num = [int(n) for n in input().split()]

    flag = -1
    ans = 0
    for i in range(N):
        if num[i] == K:
            flag = i
        elif flag != -1 and i - flag != K - num[i]:
            flag = -1
        elif flag != -1 and i - flag == K - 1:
            ans += 1
            flag = -1

    print(f"Case #{t + 1}: {ans}")
