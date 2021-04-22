# Introductions Organization
# https://codingcompetitions.withgoogle.com/codejamio/round/00000000004360f2/000000000077796b
# Convert the problem to graph, introduction: two nodes are connected with a intermediate manager node, after introduction, two nodes are directly connected
# Two nodes can eventually know each other if there exists a path with all manager intermediate nodes, call initial shortest # egdes = x, goal is to make x become 1
# If only 1 introduction can happen in one time slot, the required # time slot is x - 1
# Considering simultaneous introduction and no duplicate member, one time slot can make at most ceil((x - 1) / 3) introduction, find the # time slot such that x -> x - ceil((x - 1) / 3) until 1
# Use Floyd–Warshall algorithm to find the shortest path (with only intermediate manager nodes) between each two nodes
# https://en.wikipedia.org/wiki/Floyd%E2%80%93Warshall_algorithm
# O(M * (M + N)^2 + P)

import math

INT_MAX = 1000

T = int(input())
for t in range(T):
    [M, N, P] = [int(n) for n in input().split()]
    graph = [[INT_MAX] * (M + N) for i in range(M + N)]
    pairs = []
    for i in range(M + N):
        temp = input()
        for j in range(M + N):
            if temp[j] == 'Y':
                graph[i][j] = 1
                graph[j][i] = 1
    for i in range(P):
        pairs.append([int(n) for n in input().split()])
    # print(graph)
    # print(pairs)

    result = []
    result_cache = {}
    # Floyd–Warshall algorithm, check if (graph[i][j] > graph[i][k] + graph[k][j])
    for k in range(M):
        for i in range(M + N):
            for j in range(M + N):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    # print(graph)
    for i in range(P):
        if graph[pairs[i][0] - 1][pairs[i][1] - 1] == INT_MAX:
            result.append(-1)
        else:
            x = graph[pairs[i][0] - 1][pairs[i][1] - 1]
            if x in result_cache:
                result.append(result_cache[x])
            else:
                count = 0
                temp_x = x
                while temp_x > 1:
                    temp_x = temp_x - math.ceil((temp_x - 1) / 3)
                    count += 1
                result.append(count)
                result_cache[x] = count

    print(f"Case #{t + 1}: {' '.join([str(n) for n in result])}")
