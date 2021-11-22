# Checksum
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000436140/000000000068c2c3
# For any row / column remaining one unknown element, it can be revealed with checksum
# Convert the original problem to weighted bipartite graph, row / column numbers is a party
# There's a edge Bij if it's unknown in matrix, a row / column remaining one unknown element means a node with exact one edge
# If the graph is forest-like (i.e. no cycle) we can remove the edge from leaf (leaf edge means it's the only edge of some node) until we clean whole forest
# If the gragh has cycle, we need to find the minimum set of edges to break the cycle
# Method 2: Convert the problem to finding max weight spanning forest https://en.wikipedia.org/wiki/Minimum_spanning_tree
# We need to make the graph fully connected by adding complement set of edge with weight 0
# After finding the Max Spanning Tree, the edges not chosen are the ones need to be removed
# Using Prim's algorithm with dense graph, O(N^2)

T = input()
for t in range(int(T)):
    N = int(input())
    matrixA = []
    matrixB = []
    checksumR = []
    checksumC = []
    total_weight = 0
    for i in range(N):
        matrixA.append([int(n) for n in input().split()])
    for i in range(N):
        matrixB.append([int(n) for n in input().split()])
        total_weight += sum(matrixB[i])
    checksumR = [int(n) for n in input().split()]
    checksumC = [int(n) for n in input().split()]

    # Use Prim's algorithm to find Max Spanning Tree
    max_weight = 0
    # max_edges[i] = (j, w) means the from a not-selected node i, the max edge to a selected-node j with weight w
    # First N nodes mean row 0 ~ N-1, second N nodes mean col 0 ~ N-1
    max_edge = [(-1, 0)] * (2 * N)
    selected = [False] * (2 * N)
    for i in range(2 * N):
        next_node = -1
        for j in range(2 * N):
            if (not selected[j] and (next_node == -1 or max_edge[j][1] > max_edge[next_node][1])):
                next_node = j
        # print(next_node)
        selected[next_node] = True
        max_weight += max_edge[next_node][1]
        if (next_node < N):
            for j in range(N, 2 * N):
                if matrixB[next_node][j - N] > max_edge[j][1]:
                    max_edge[j] = (next_node, matrixB[next_node][j - N])
        else:
            for j in range(0, N):
                if matrixB[j][next_node - N] > max_edge[j][1]:
                    max_edge[j] = (next_node, matrixB[j][next_node - N])

    print("Case #{}: {}".format(t + 1, total_weight - max_weight))
