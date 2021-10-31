# Beauty of tree
# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff08/0000000000386edd
# O(N)

T = int(input())
for t in range(T):
    [N, A, B] = [int(n) for n in input().split()]
    parent = [int(n) for n in input().split()]

    children = [[] for i in range(N + 1)]
    for i in range(N - 1):
        children[parent[i]].append(i + 2)
    # print(children)

    # DFS to check all path
    path = [1]
    checked = [False] * (N + 1)
    A_pass = [0] * (N + 1) # A_pass[i]: How many times the node i is picked across all path
    B_pass = [0] * (N + 1)
    while path:
        all_children_passed = True
        for child in children[path[-1]]:
            if not checked[child]:
                path.append(child)
                all_children_passed = False
                break
        if all_children_passed:
            A_pass[path[-1]] += 1
            if len(path) > A:
                A_pass[path[-1-A]] += A_pass[path[-1]]
            B_pass[path[-1]] += 1
            if len(path) > B:
                B_pass[path[-1-B]] += B_pass[path[-1]]
            checked[path[-1]] = True
            path.pop(-1)
    # print(A_pass)
    # print(B_pass)

    # For each node, P(passed by A or B) = P(passed by A) + P(passed by B) - P(passed by A and B)
    ans = 0
    for i in range(1, N + 1):
        ans += A_pass[i] / N + B_pass[i] / N - (A_pass[i] * B_pass[i]) / (N * N)
    print(f"Case #{t + 1}: {ans}")
