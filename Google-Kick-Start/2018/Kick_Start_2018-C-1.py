# Planet Distance
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050ee0/0000000000051005

import copy

T = int(input())
for t in range(T):
    N = int(input())
    graph = [set() for _ in range(N)]
    for _ in range(N):
        [v, w] = [int(x) for x in input().split()]
        graph[v-1].add(w-1)
        graph[w-1].add(v-1)
    # print(graph)

    # Find the nodes of cycle
    # Option 1: Use DFS
    # prev = [-1] * N
    # stack = [0]
    # checked = set()
    # path = []
    # while stack:
    #     # print(stack)
    #     v = stack.pop(-1)
    #     if v in checked:
    #         continue
    #     checked.add(v)
    #     for w in graph[v]:
    #         if w not in checked:
    #             stack.append(w)
    #             prev[w] = v
    #         elif w != prev[v]: # Reach visited point but it's not parent, cycle found!
    #             prev[w] = v
    #             path.append(v)
    #             stack.clear()
    #             break
    # last = prev[path[0]]
    # while last != path[0]:
    #     path.append(last)
    #     last = prev[last]
    # print(path)

    # Option 2: By "trimming" the nodes with only one edge
    degree = {}
    for i in range(N):
        degree[i] = len(graph[i])
    # print(degree)

    graph2 = copy.deepcopy(graph)
    queue = set()
    for (k, v) in degree.items():
        if v == 1:
            queue.add(k)
    while queue:
        # print(queue)
        for v in queue:
            w = list(graph2[v])[0]
            # print(v, w)
            degree[w] -= 1
            graph2[v].clear()
            graph2[w].remove(v)
            degree.pop(v)
        queue.clear()
        for (k, v) in degree.items():
            if v == 1:
                queue.add(k)
    path = degree.keys()
    # print(path)

    # Use BFS to find the distance between cycle
    ans = [-1] * N
    path = set(path)
    dist = 0
    unchecked = set(range(N))
    while unchecked:
        next = set()
        for v in path:
            unchecked.remove(v)
            ans[v] = dist
            for w in graph[v]:
                if w in unchecked and w not in path:
                    next.add(w)
        dist += 1
        path = next

    print(f"Case #{t + 1}: {' '.join(map(str, ans))} ")
