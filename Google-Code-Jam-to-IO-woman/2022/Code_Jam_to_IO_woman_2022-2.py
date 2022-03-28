# Ingredient Optimization
# https://codingcompetitions.withgoogle.com/codejamio/round/00000000009d9870/0000000000a341ec

import heapq

T = int(input())
for t in range(T):
    [D, N, U] = [int(x) for x in input().split()]
    deliveries = []
    for _ in range(D):
        [M, L, E] = [int(x) for x in input().split()]
        deliveries.append((M, L, E))
    orders = [int(x) for x in input().split()]

    ans = 0
    leaves = []
    flag_d = 0
    flag_o = 0
    while flag_o < N:
        # print(leaves)
        if flag_d < D and deliveries[flag_d][0] <= orders[flag_o]:
            for i in range(deliveries[flag_d][1]):
                heapq.heappush(leaves, deliveries[flag_d][0] + deliveries[flag_d][2])
            flag_d += 1
        else:
            used = 0
            while leaves and used < U:
                if leaves[0] > orders[flag_o]:
                    used += 1
                heapq.heappop(leaves)
            if used == U:
                ans += 1
                flag_o += 1
            else:
                break

    print(f"Case #{t + 1}: {ans}")
