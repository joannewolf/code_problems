# Interesting Outing
# https://codingcompetitions.withgoogle.com/codejamio/round/00000000009d9870/0000000000a33bc7
# Key idea: For any fixed root, it only matters that which subtree is the last visited
# Cuz in the last-visited subtree, we might not need to traverse all edges twice
# O(N^2), for each node as root, get cost needs O(N), RE on test set 2 for too deep recursion

INF = pow(10, 12) + 1

# For a subtree rooted at root, and root coming from source, calculate the min cost
def get_cost(source: int, root: int):
    child = neighbor[root].copy()
    child.discard(source)
    if not child:
        return 0

    # Calculate the sum of double edges (go and back) for all subtree edges
    total_double_edges = 0
    double_edges = {}
    for c in child:
        checked = set([root])
        queue = [c]
        sum = 2 * edge[root][c]
        while queue:
            now = queue.pop(0)
            checked.add(now)
            for next in neighbor[now]:
                if next not in checked:
                    sum += 2 * edge[now][next]
                    queue.append(next)
        double_edges[c] = sum
        total_double_edges += sum

    min_cost = INF
    for c in child:
        cost = get_cost(root, c) + edge[root][c] + (total_double_edges - double_edges[c])
        if cost < min_cost:
            min_cost = cost
    return min_cost


T = int(input())
for t in range(T):
    N = int(input())
    edge = [[-1] * N for _ in range(N)]
    neighbor = [set() for _ in range(N)]
    for _ in range(N - 1):
        [A, B, C] = [int(x) for x in input().split()]
        edge[A - 1][B - 1] = C
        edge[B - 1][A - 1] = C
        neighbor[A - 1].add(B - 1)
        neighbor[B - 1].add(A - 1)

    ans = INF
    for root in range(N):
        cost = get_cost(-1, root)
        # print("root", root, "cost", cost)
        if cost < ans:
            ans = cost
    print(f"Case #{t + 1}: {ans}")
