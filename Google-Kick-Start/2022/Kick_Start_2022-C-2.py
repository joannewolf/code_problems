# Range Partition
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000008cb4d1/0000000000b20deb

T = int(input())
for t in range(T):
    [N, X, Y] = [int(x) for x in input().split()]

    if (N * (N+1) // 2) % (X + Y) != 0:
        print(f"Case #{t + 1}: IMPOSSIBLE")
    else:
        print(f"Case #{t + 1}: POSSIBLE")
        n = (N * (N+1) // 2) // (X + Y)
        X *= n
        ans = []
        flag = N
        while X:
            if flag <= X:
                ans.append(flag)
                X -= flag
                flag -= 1
            else:
                ans.append(X)
                X = 0

        print(len(ans))
        print(' '.join(map(str, ans)))
