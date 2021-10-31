# Beauty of tree
# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff08/0000000000386edd
# O(N^2), MLE on test set 2

T = int(input())
for t in range(T):
    [N, A, B] = [int(n) for n in input().split()]
    parent = [int(n) for n in input().split()]

    path = [[1]]
    for i in range(N - 1):
        path.append(path[parent[i] - 1] + [i + 2])
    # print(path)

    A_picks = [set([1])] # A_picks[i]: starting from node i, what are the nodes picked until root
    B_picks = [set([1])]
    for i in range(1, N):
        if len(path[i]) > A:
            A_picks.append(A_picks[path[i][-1-A] - 1].union([i + 1]))
        else:
            A_picks.append(set([i + 1]))
        if len(path[i]) > B:
            B_picks.append(B_picks[path[i][-1-B] - 1].union([i + 1]))
        else:
            B_picks.append(set([i + 1]))
    # print(A_picks)
    # print(B_picks)

    ans = 0
    for i in range(N):
        for j in range(N):
            ans += len(A_picks[i].union(B_picks[j]))
    print(f"Case #{t + 1}: {ans / (N * N)}")
