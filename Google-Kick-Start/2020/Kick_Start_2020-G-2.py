# Maximum Coins
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000001a0069/0000000000414a23

T = int(input())
for t in range(T):
    N = int(input())
    coin = []
    for i in range(N):
        coin.append([int(n) for n in input().split()])

    ans = 0
    for i in range(N):
        sum = 0
        r = 0
        c = i
        while r < N and c < N:
            sum += coin[r][c]
            r += 1
            c += 1
        ans = max(ans, sum)

    for i in range(1, N):
        sum = 0
        r = i
        c = 0
        while r < N and c < N:
            sum += coin[r][c]
            r += 1
            c += 1
        ans = max(ans, sum)

    print(f"Case #{t + 1}: {ans}")
