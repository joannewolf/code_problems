# Cherries Mesh
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050edb/0000000000170721

T = int(input())
for t in range(T):
    [N, M] = [int(n) for n in input().split()]
    graph = [set() for _ in range(N)]
    for i in range(M):
        [c, d] = [int(n) for n in input().split()]
        graph[c - 1].add(d - 1)
        graph[d - 1].add(c - 1)

    unchecked = set(range(N))
    group_count = 0
    while unchecked:
        queue = set([next(iter(unchecked))])
        while queue:
            # print(queue)
            v = next(iter(queue))
            queue.remove(v)
            unchecked.remove(v)
            for w in graph[v]:
                if w in unchecked and w not in queue:
                    queue.add(w)
        group_count += 1

    ans = (group_count - 1) * 2 + (N - group_count)
    print(f"Case #{t + 1}: {ans}")
