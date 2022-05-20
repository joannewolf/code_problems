# Cards Game
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000201b7d/0000000000201c9c
# O(N^2)

INF = pow(10, 10)

T = int(input())
for t in range(T):
    N = int(input())
    red = [int(x) for x in input().split()]
    blue = [int(x) for x in input().split()]

    dist = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i != j:
                dist[i][j] = min(red[i] ^ blue[j], blue[i] ^ red[j])

    # Use Prim's algorithm to find the dist sum of minimum spanning tree
    ans = 0
    cost = [INF] * N
    connection = [-1] * N
    not_checked = set(range(N))
    while not_checked:
        min_edge = INF + 1
        next_v = -1
        for v in not_checked:
            if cost[v] < min_edge:
                min_edge = cost[v]
                next_v = v
        if connection[next_v] != -1:
            ans += dist[next_v][connection[next_v]]
        not_checked.remove(next_v)
        # For the remaining not-checked nodes, update their minimum cost to current MST
        for v in not_checked:
            if dist[next_v][v] < cost[v]:
                cost[v] = dist[next_v][v]
                connection[v] = next_v

    print(f"Case #{t + 1}: {ans}")
