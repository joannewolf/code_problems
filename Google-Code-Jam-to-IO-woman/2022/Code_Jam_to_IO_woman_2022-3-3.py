# Interesting Outing
# https://codingcompetitions.withgoogle.com/codejamio/round/00000000009d9870/0000000000a33bc7
# Key idea: For starting and ending point (S, T), if extending this path to also walk back from T to S at the end
# It's exactly distance(S, T) longer than the length of the walk that visits all the places
# The optimal enclosed path is to use 2 * sum{edge}

T = int(input())
for t in range(T):
    N = int(input())
    total_double_edge = 0
    edge = [[-1] * N for _ in range(N)]
    neighbor = [set() for _ in range(N)]
    for _ in range(N - 1):
        [A, B, C] = [int(x) for x in input().split()]
        total_double_edge += 2 * C
        edge[A - 1][B - 1] = C
        edge[B - 1][A - 1] = C
        neighbor[A - 1].add(B - 1)
        neighbor[B - 1].add(A - 1)

    max_path = 0
    # Use DFS to find max path between node pair
    for start in range(N):
        dist = [-1] * N # dist[i]: distance from start to i
        prev = [-1] * N
        dist[start] = 0
        checked = set()
        queue = [start]
        while queue:
            now = queue.pop(0)
            checked.add(now)
            for next in neighbor[now]:
                if next not in checked:
                    prev[next] = now
                    dist[next] = dist[now] + edge[now][next]
                    queue.append(next)
        if max(dist) > max_path:
            max_path = max(dist)

    ans = total_double_edge - max_path
    print(f"Case #{t + 1}: {ans}")
