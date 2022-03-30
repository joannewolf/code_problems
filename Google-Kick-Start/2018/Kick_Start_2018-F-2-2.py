# Specializing Villages
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050e07/0000000000051134
# Key idea: Define d(v) as distance of shortest neighbor road, f(v) means the other village connected by shortest neighbor road
# After sorting the villages by increasing d(v), we assign v the opposite food of f(v); if f(v) doesn't have a food assigned, we can assign either food to v
# If a 0-length road connects villages x and y, any village v f(v) = x or y has two choices, it can get one food through r(v) and the other from a combination of r(v) and the 0-length road
# Cuz 0-length road must be the shortest neighbor road for x and y, the x and y must have different product
# Ans = 2^N, N = {v | f(f(v)) = v and l(f(v)) > l(v)} ∪ {v | d(v) > 0 and d(f(v)) = 0}
# O(VlogV)

INF = pow(10, 7)

T = int(input())
for t in range(T):
    [V, E] = [int(x) for x in input().split()]
    dist = [[INF] * V for _ in range(V)]
    neighbor = [set() for _ in range(V)]
    for _ in range(E):
        [a, b, l] = [int(x) for x in input().split()]
        dist[a - 1][b - 1] = l
        dist[b - 1][a - 1] = l
        neighbor[a - 1].add(b - 1)
        neighbor[b - 1].add(a - 1)

    d = [] # d(v): distance of shortest neighbor road
    f = [] # f(v): the other village connected by shortest neighbor road
    villages = [] # Tuple (v, d(v))
    for v in range(V):
        min_edge = INF
        min_neighbor = -1
        for w in neighbor[v]:
            if dist[v][w] < min_edge:
                min_edge = dist[v][w]
                min_neighbor = w
        d.append(min_edge)
        f.append(min_neighbor)
        villages.append((v, min_edge))
    villages.sort(key=lambda x: x[1])

    n = 0
    for (v, _) in villages:
        if (f[v] > v and f[f[v]] == v) or (d[v] > 0 and d[f[v]] == 0):
            n += 1

    print(f"Case #{t + 1}: {pow(2, n)}")
