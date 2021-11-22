# Bus Routes
# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ffc8/00000000002d83bf

T = int(input())
for t in range(T):
    [N, D] = [int(n) for n in input().split()]
    X = [int(n) for n in input().split()]

    ans = D
    for i in range(N - 1, -1, -1):
        if ans % X[i] != 0:
            ans = (ans // X[i]) * X[i]

    print(f"Case #{t + 1}: {ans}")
