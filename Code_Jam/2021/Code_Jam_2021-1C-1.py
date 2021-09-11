# Closest Pick
# https://codingcompetitions.withgoogle.com/codejam/round/00000000004362d7/00000000007c0f00

import math

T = int(input())
for t in range(T):

    [N, K] = [int(n) for n in input().split()]
    sold_tickets = [int(n) for n in input().split()]

    # Get sorted unique sold tickets, P_1, ..., P_N
    sold_tickets = sorted(list(set(sold_tickets)))
    
    # If choosing number < P_1, the optimal choice is to choose P_1 - 1, and will win when c = 1 ~ P_1-1
    # If choosing P_i < number < P_{i+1}, the optimal choice is to choose P_i + 1 or P_{i+1} - 1, and will win when c = P_i + 1 ~ floor((P_i + P_{i+1}) / 2) or ceil((P_i + P_{i+1}) / 2) ~ P_{i+1} - 1
    # If choosing number > P_N, the optimal choice is to choose P_N + 1, and will win when c = P_N + 1 ~ K
    # Eventually find the max 2 choices because we're purchasing 2 tickets
    intervals = []
    intervals.append(sold_tickets[0] - 1)
    intervals.append(K - sold_tickets[-1])
    for i in range(0, len(sold_tickets) - 1):
        gap = sold_tickets[i+1] - sold_tickets[i] - 1
        intervals.append(math.ceil(gap / 2))
        intervals.append(math.floor(gap / 2))
    intervals.sort(reverse=True)

    result = (intervals[0] + intervals[1]) / K

    print("Case #{}: {}".format(t + 1, result))
