# Food Stalls
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000051061/0000000000161476
# Assume we choose (K+1) spots from N, the optimize warehouse location must be the median spot
# For each possible warehouse location, we use heap to find the min left (K // 2) costs and right (K - K // 2) costs
# Possible warehouse location is between [K // 2, N - (K - K // 2) - 1]
# O(NlogK)

import heapq

INT_MAX = pow(10, 15)
T = int(input())
for t in range(T):
    [K, N] = [int(n) for n in input().split()]
    X = [int(n) for n in input().split()]
    C = [int(n) for n in input().split()]
    spots = []
    for i in range(N):
        spots.append((X[i], C[i]))
    spots.sort()

    left_half = K // 2
    right_half = K - left_half
    left_cost = [0] * N
    right_cost = [0] * N

    # For each possible warehouse location, calculate min left K // 2 costs
    # Use negative number to achieve max heap
    heap = [-(c + spots[-1][0] - x) for (x, c) in spots[0:left_half]]
    heapq.heapify(heap)
    heap_sum = -sum(heap)
    left_cost[left_half] = heap_sum - left_half * (spots[-1][0] - spots[left_half][0])
    for i in range(left_half + 1, N - right_half):
        if left_half == 0: # No stall needed on warehouse's left side
            break
        new_stall_cost = spots[i - 1][1] + spots[-1][0] - spots[i - 1][0]
        if -new_stall_cost > heap[0]:
        # New stall cost is less than the current max cost, so drop current max
            curr_max = -heapq.heappop(heap)
            heapq.heappush(heap, -new_stall_cost)
            heap_sum = heap_sum - curr_max + new_stall_cost
        left_cost[i] = heap_sum - left_half * (spots[-1][0] - spots[i][0])

    # For each possible warehouse location, calculate min right N - (K // 2) costs
    heap = [-(c + x - spots[-1][0]) for (x, c) in spots[N - right_half:]]
    heapq.heapify(heap)
    heap_sum = -sum(heap)
    right_cost[N - right_half - 1] = heap_sum + right_half * (spots[-1][0] - spots[N - right_half - 1][0])
    for i in range(N - right_half - 2, left_half - 1, -1):
        new_stall_cost = spots[i + 1][1] + spots[i + 1][0] - spots[-1][0]
        if -new_stall_cost > heap[0]:
        # New stall cost is less than the current max cost, so drop current max
            curr_max = -heapq.heappop(heap)
            heapq.heappush(heap, -new_stall_cost)
            heap_sum = heap_sum - curr_max + new_stall_cost
        right_cost[i] = heap_sum + right_half * (spots[-1][0] - spots[i][0])

    # print(left_cost)
    # print(right_cost)
    ans = INT_MAX
    for i in range(N):
        if right_cost[i] != 0 and left_cost[i] + right_cost[i] + spots[i][1] < ans:
            ans = left_cost[i] + right_cost[i] + spots[i][1]

    print(f"Case #{t + 1}: {ans}")
