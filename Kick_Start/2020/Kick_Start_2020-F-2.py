# Metal Harvest
# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff48/00000000003f4b8b
# DP, O(N^3), MLE on test set 2

import math

T = int(input())
for t in range(T):
    [N, K] = [int(n) for n in input().split()]
    intervals = []
    for i in range(N):
        [s, e] = [int(n) for n in input().split()]
        intervals.append((s, e))

    intervals.sort()
    # print(intervals)
    deploy = [[-1] * N for _ in range(N)] # deploy[i][j]: the minimum deploy time for interval i to j (inclusive)
    for i in range(N):
        deploy[i][i] = math.ceil((intervals[i][1] - intervals[i][0]) / K)

    for i in range(1, N):
        for start in range(N - i):
            # print(start, start + i)
            min_deploy = math.ceil((intervals[start + i][1] - intervals[start][0]) / K)
            for cut in range(start, start + i):
                # print("*", start, cut, cut + 1, start + i)
                min_deploy = min(min_deploy, deploy[start][cut] + deploy[cut + 1][start + i])
            deploy[start][start + i] = min_deploy
    # for i in range(N):
    #     print(deploy[i])

    print(f"Case #{t + 1}: {deploy[0][N - 1]}")
