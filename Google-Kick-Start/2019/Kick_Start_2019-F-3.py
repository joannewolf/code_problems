# Spectating Villages
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050edc/000000000018666b
# All nodes will form a tree, since there's only V-1 edges
# Define F(K, P, Q) = max beauty of subtree of node K (including K)
# P = 0/1 whether parent has lighthouse; Q = 0/1 whether node K itself has lighthouse
# Case 1: Q = 1, node K itself has lighthouse
#   F(K, P, Q) = B_K + SUM{max(F(C, 1, 0), F(C, 1, 1))} for all children C of K
# Case 2: Q = 0, P = 1, node K's parent has lighthouse, so node K must be illuminated
#   F(K, P, Q) = B_K + SUM{max(F(C, 0, 0), F(C, 0, 1))} for all children C of K
# Case 3: Q = 0, P = 0, node K's parent and itself both not have lighthouse, check whether K's children has lighthouse
#   F(K, P, Q) = max{dp(M, 1) + B_K, dp(M, 0)}, M = # of children of K
#   dp(i, j) = max beauty of first i subtrees of K; j = 0/1 whether exists at least one lighthouse in first i children
#   dp(i, 0) = dp(i-1, 0) + F(Ci, 0, 0), K doesn't have lighthouse, i-th children doesn't have lighthouse
#   dp(i, 1) = max{ dp(i-1, 1) + max{F(Ci, 0, 1), F(Ci, 0, 0)} lighthouse appear before
#                   dp(i-1, 0) + F(Ci, 0, 1) lighthouse appear at i-th children }
# O(V), TLE but correct locally on test set 2

T = int(input())
for t in range(T):
    V = int(input())
    beauty = [int(x) for x in input().split()]
    edges = [set() for _ in range(V)]
    for i in range(V-1):
        [v, w] = [int(x) for x in input().split()]
        edges[v - 1].add(w - 1)
        edges[w - 1].add(v - 1)

    unchecked = set(range(V))
    children = [[] for _ in range(V)]
    queue = [0] # Set node 0 as root
    while unchecked:
        current = queue.pop(0)
        unchecked.remove(current)
        for neighbor in edges[current]:
            if neighbor in unchecked:
                children[current].append(neighbor)
                queue.append(neighbor)
    # for i in range(V):
    #     print(children[i])

    F = [[[0] * 2 for _ in range(2)] for _ in range(V)]
    unchecked = set(range(V))
    stack = [0]
    while unchecked:
        current = stack[-1]
        if not children[current]: # Leaf node
            F[current][0][0] = 0
            F[current][0][1] = beauty[current]
            F[current][1][0] = beauty[current]
            F[current][1][1] = beauty[current]
            stack.pop(-1)
            unchecked.remove(current)
        elif children[current][0] in unchecked:
        # If children not yet processed, process children first
            stack.extend(children[current])
        else:
            # Case 1: Q = 1
            sum = beauty[current]
            for c in children[current]:
                sum += max(F[c][1][0], F[c][1][1])
            F[current][0][1] = sum
            F[current][1][1] = sum

            # Case 2: Q = 0, P = 1
            sum = beauty[current]
            for c in children[current]:
                sum += max(F[c][0][0], F[c][0][1])
            F[current][1][0] = sum

            # Case 3: Q = 0, P = 0
            M = len(children[current])
            C = children[current]
            dp = [[0] * 2 for _ in range(M)]
            dp[0][0] = F[C[0]][0][0]
            dp[0][1] = F[C[0]][0][1]
            for i in range(1, M):
                dp[i][0] = dp[i-1][0] + F[C[i]][0][0]
                dp[i][1] = max(
                    dp[i-1][1] + max(F[C[i]][0][1], F[C[i]][0][0]),
                    dp[i-1][0] + F[C[i]][0][1]
                )
            F[current][0][0] = max(dp[M-1][1] + beauty[current], dp[M-1][0])

            stack.pop(-1)
            unchecked.remove(current)

    print(f"Case #{t + 1}: {max(F[0][0][0], F[0][0][1])}")
