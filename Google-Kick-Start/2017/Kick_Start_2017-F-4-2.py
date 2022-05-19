# Catch Them All
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000201d29/0000000000201c9b
# In DP method, it only needs dp[i - 1] to calculate dp[i], we can rewrite the state transition equation
# Let S(i) = SUM{dist[i][j]}, j != i
#   +----------+   +---------------------------------------------+   +------------+
#   | dp[K, 1] |   |    0   , 1/(N-1), ... , 1/(N-1), S(1)/(N-1) |   | dp[K-1, 1] |
#   | dp[K, 2] |   | 1/(N-1),    0   , ... , 1/(N-1), S(2)/(N-1) |   | dp[K-1, 2] |
#   |   ...    | = |   ...  ,   ...  , ... ,   ...  ,     ...    | * |    ...     |
#   | dp[K, N] |   | 1/(N-1), 1/(N-1), ... ,    0   , S(N)/(N-1) |   | dp[K-1, N] |
#   |    1     |   |    0   ,    0   , ... ,    0   ,     1      |   |     1      |
#   +----------+   +---------------------------------------------+   +------------+
# Let F_K be column vector of dp[K, i], and let A denote the transition matrix
# -> F_K = A * F_(K-1) = A^K * F_0
# O(N^3 + N^3*log(P))

import math

INF = pow(10, 5)

def matrix_multi(A, B):
    assert(len(A[0]) == len(B))
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    for i in range(len(A)):
        for k in range(len(A[0])):
            for j in range(len(B[0])):
                result[i][j] += A[i][k] * B[k][j]
    return result

T = int(input())
for t in range(T):
    [N, M, P] = [int(x) for x in input().split()]
    dist = [[INF] * N for _ in range(N)]
    for i in range(N):
        dist[i][i] = 0
    for _ in range(M):
        [u, v, d] = [int(x) for x in input().split()]
        dist[u-1][v-1] = d
        dist[v-1][u-1] = d

    # Use Floyd–Warshall algorithm to find all pairs of shortest paths
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    A = [] # A[i] = base_matrix ^ (2 ^ i)
    base_matrix = []
    for i in range(N):
        dist_sum = 0
        for j in range(N):
            if j != i:
                dist_sum += dist[i][j]
        row = [1 / (N-1)] * N + [dist_sum / (N-1)]
        row[i] = 0
        base_matrix.append(row)
    base_matrix.append([0] * N + [1])
    # for i in range(N+1):
    #     print(base_matrix[i])
    A.append(base_matrix)
    
    for i in range(1, int(math.log2(P)) + 1):
        A.append(matrix_multi(A[-1], A[-1]))

    unit_matrix = []
    for i in range(N+1):
        row = [0] * (N+1)
        row[i] = 1
        unit_matrix.append(row)
    # for i in range(N+1):
    #     print(unit_matrix[i])

    A_P = unit_matrix
    for i in range(int(math.log2(P)) + 1):
        if P & 1:
            A_P = matrix_multi(A_P, A[i])
        P //= 2

    print(f"Case #{t + 1}: {A_P[0][-1]}")
