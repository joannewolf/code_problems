# H-index
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000008f4332/0000000000941e56
# Same with 2019-H-1
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050edd/00000000001a274e

import heapq

T = int(input())
for t in range(T):
    N = int(input())
    C = map(int, input().split())

    ans = []
    next_H = 2
    queue = []
    heapq.heapify(queue)
    for c in C:
        heapq.heappush(queue, c)
        while queue and queue[0] < next_H:
            heapq.heappop(queue)
        if len(queue) >= next_H:
            next_H += 1
        ans.append(next_H - 1)

    print(f"Case #{t + 1}: {' '.join(map(str, ans))}")
