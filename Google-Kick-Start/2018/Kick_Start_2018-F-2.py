# Specializing Villages
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050e07/0000000000051134
# Brute-force, O(2^V * V^2), TLE on test set 2

INF = pow(10, 7)

T = int(input())
for t in range(T):
    [V, E] = [int(x) for x in input().split()]
    dist = [[INF] * V for _ in range(V)]
    for _ in range(E):
        [a, b, l] = [int(x) for x in input().split()]
        dist[a - 1][b - 1] = l
        dist[b - 1][a - 1] = l
    for i in range(V):
        dist[i][i] = 0
    # Use Floyd–Warshall algorithm to find shortest distance between all pairs of node
    for k in range(V):
        for i in range(V):
            for j in range(V):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    # for i in range(V):
    #     print(dist[i])

    min_cost = INF
    min_count = 0
    # Emurate 2^V plans, bit 0 means producing fruit, bit 1 means producing veg
    for plan in range(pow(2, V)):
        product = bin(plan)[2:].zfill(V)
        # Calculate min cost for current plan
        cost_sum = 0
        possible = True
        for v in range(V):
            min_dist = INF # Min dist for village v to find another food
            for w in range(V):
                if product[v] != product[w] and dist[v][w] < min_dist:
                    min_dist = dist[v][w]
            if min_dist != INF:
                cost_sum += min_dist
            else: # Means village v cannot get another food
                possible = False
                break
        if possible:
            # print(product, cost_sum)
            if cost_sum < min_cost:
                min_cost = cost_sum
                min_count = 1
            elif cost_sum == min_cost:
                min_count += 1

    # print(min_cost, min_count)
    print(f"Case #{t + 1}: {min_count}")
