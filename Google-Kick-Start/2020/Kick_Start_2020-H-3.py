# Rugby
# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff49/000000000043b027
# The optimal solution will have players keep their original relative X order
# O(NlogN)

T = int(input())
for t in range(T):
    N = int(input())
    X = []
    Y = []
    for i in range(N):
        [x, y] = [int(n) for n in input().split()]
        X.append(x)
        Y.append(y)

    X.sort()
    for i in range(N):
        X[i] -= i # This is the optimal first X to all players, so that they don't need to move
    X.sort()
    Y.sort()

    # Find median of optimal Y and optimal first X
    if N % 2 == 1:
        final_x = X[N // 2]
        final_y = Y[N // 2]
    else:
        final_x = (X[N // 2] + X[N // 2 - 1]) // 2
        final_y = (Y[N // 2] + Y[N // 2 - 1]) // 2

    ans = 0
    for i in range(N):
        ans += abs(X[i] - final_x)
        ans += abs(Y[i] - final_y)

    print(f"Case #{t + 1}: {ans}")
