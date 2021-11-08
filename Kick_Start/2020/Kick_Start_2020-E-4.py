# Golden Stone
# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff47/00000000003bef29
# The problem can be translated to a graph question
# Consider each {junction, stone} as a vertex, for each street (u, v), there will be new S edges {(u, s), (v, s)} for each stone type s
# The goal is to find the optimal cost{u, 1} over all junctions
# If a stone type s is given available in junction u, cost{u, s} = 0
# Using Bellman–Ford or Dijkstra's algorithm to find the optimal cost, imagine a virtual single source, and the distance to each vertex is the cost
# V = N * S, E = M * S, O((E + V + R*N)logV) = O((N*S + M*S + R*N)log(N*S)) 

import heapq

INF = pow(10, 12)
T = int(input())
for t in range(T):
    [N, M, S, R] = [int(n) for n in input().split()]
    V = N * S # There are N * S vertices for all {junction, stone} combinations
    cost = [INF] * V # cost[i]: juction i // S, stone type i % S
    not_checked = set(range(V))
    edges = set()
    recipes = []
    for i in range(M):
        [u, v] = [int(n) for n in input().split()]
        for j in range(S):
            edges.add((S * (u - 1) + j, S * (v - 1) + j))
            edges.add((S * (v - 1) + j, S * (u - 1) + j))
    for i in range(N):
        stones = [int(n) - 1 for n in input().split()]
        for s in stones[1:]:
            cost[S * i + s] = 0
    for i in range(R):
        temp = [int(n) - 1 for n in input().split()]
        recipes.append((temp[-1], temp[1:-1]))

    # Dijkstra's algorithm
    pq = [(cost[i], i) for i in range(V)]
    heapq.heapify(pq)
    while not_checked:
        while True:
            (c, u) = heapq.heappop(pq)
            if u in not_checked:
                break
        not_checked.remove(u)
        # Reduce cost{v, s} by carrying stone s from j to v.
        for v in not_checked:
            if (u, v) in edges and c + 1 < cost[v]:
                cost[v] = c + 1
                heapq.heappush(pq, (c + 1, v))
        # Reduce cost {j, stone} by applying recipes where s is ingredient
        j = u // S
        s = u % S
        for (target, material) in recipes:
            if s in material:
                new_cost = sum(cost[j * S + m] for m in material)
                if new_cost < cost[j * S + target]:
                    cost[j * S + target] = new_cost
                    heapq.heappush(pq, (new_cost, j * S + target))

    min_energy = min(cost[S * i] for i in range(N))
    if min_energy == INF:
        print(f"Case #{t + 1}: -1")
    else:
        print(f"Case #{t + 1}: {min_energy}")
