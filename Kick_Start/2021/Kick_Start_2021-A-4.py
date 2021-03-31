# Checksum
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000436140/000000000068c2c3
# For any row / column remaining one unknown element, it can be revealed with checksum
# Convert the original problem to weighted bipartite graph, row / column numbers is a party
# There's a edge Bij if it's unknown in matrix, a row / column remaining one unknown element means a node with exact one edge
# If the graph is forest-like (i.e. no cycle) we can remove the edge from leaf (leaf edge means it's the only edge of some node) until we clean whole forest
# If the gragh has cycle, we need to find the minimum set of edges to break the cycle
# Method 1: iterate all edges in non-decreasing order and find if it's part of cycle (using DFS), if so, remove current edge
# O(N^2 edge * N^2 doing DFS) = O(N^4), pass test set 1

def in_cycle(path):
    # print(path, graph[path[-1]])
    for next_node in graph[path[-1]]:
        if (len(path) > 2 and next_node == path[0]):
            return True
        elif (next_node not in path):
            new_path = path + [next_node]
            if in_cycle(new_path):
                return True
    return False

T = input()
for t in range(int(T)):
    N = int(input())
    matrixA = []
    matrixB = []
    checksumR = []
    checksumC = []
    for i in range(N):
        matrixA.append([int(n) for n in input().split()])
    for i in range(N):
        matrixB.append([int(n) for n in input().split()])
    checksumR = [int(n) for n in input().split()]
    checksumC = [int(n) for n in input().split()]

    graph = [[] for i in range(2 * N)] # first N nodes mean row 0 ~ N-1, second N nodes mean col 0 ~ N-1
    edges = []
    for i in range(N):
        for j in range(N):
            if (matrixA[i][j] == -1):
                graph[i].append(N + j)
                graph[N + j].append(i)
                edges.append((matrixB[i][j], i, j))
    edges.sort(key=lambda x: x[0])
    # print(graph)
    # print(edges)

    result = 0
    for edge in edges:
        if in_cycle([edge[1], N + edge[2]]):
            # print(edge[1], N + edge[2], "in cycle")
            result += edge[0]
            matrixA[edge[1]][edge[2]] = 2
            graph[edge[1]].remove(N + edge[2])
            graph[N + edge[2]].remove(edge[1])

    print("Case #{}: {}".format(t + 1, result))
