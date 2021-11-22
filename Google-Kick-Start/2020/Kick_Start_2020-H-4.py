# Friends
# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff49/000000000043aee7
# Use Floyd–Warshall algorithm to find all pair of shortest paths between people
# O(N^3 + Q), TLE on test set 2

INF = pow(10, 5)
T = int(input())
for t in range(T):
    [N, Q] = [int(n) for n in input().split()]
    names = input().split()

    dist= [[INF] * N for i in range(N)]
    for i in range(N):
        dist[i][i] = 0
        names[i] = set(names[i])
    for i in range(N):
        for j in range(i + 1, N):
            if names[i].intersection(names[j]):
                dist[i][j] = 1
                dist[j][i] = 1
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    ans = []
    for i in range(Q):
        [x, y] = [int(n) for n in input().split()]
        temp = dist[x - 1][y - 1] + 1 if dist[x - 1][y - 1] != INF else -1
        ans.append(temp)

    print(f"Case #{t + 1}: {' '.join([str(n) for n in ans])}")
