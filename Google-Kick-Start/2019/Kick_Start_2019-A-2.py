# Parcels
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050e01/000000000006987d
# Same with 2022-Prac2-5
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000008f4a94/0000000000b55465
# O(RC*log(R+C))
# TIPS: Transform optimization problems into decision problems
# For given distance k, check if we can find a new office location which makes max delivery time at most k
# For all squares which currently have distance > k, bound an area with max distance k, ans check if we can find a intersection of all bounded areas
# To check if two points are having distance <= k, given one point's coordinate (x1, y1)
# There exists limitation that x1 + y1 - k <= x2 + y2 <= x1 + y1 + k and x1 - y1 - k <= x2 - y2 <= x1 - y1 + k
# Check if we can find a square within (0, 0) ~ (R-1, C-1) satisfying the conditions, i.e. new office location
# Then use binary search to find the minimum k which return exist_valid_office() as True

INF = 1000
def exist_valid_office(k):
    max1 = INF # upper bound for (x2 + y2)
    min1 = -INF # lower bound for (x2 + y2)
    max2 = INF # upper bound for (x2 - y2)
    min2 = -INF # lower bound for (x2 - y2)
    for list in square_dist[k+1:]:
        for (i, j) in list:
            max1 = min(max1, i + j + k)
            min1 = max(min1, i + j - k)
            max2 = min(max2, i - j + k)
            min2 = max(min2, i - j - k)

    # print(k, max1, min1, max2, min2)
    # min1 <= (x2 + y2) <= max1, min2 <= (x2 - y2) <= max2, check if we can find a square within (0, 0) ~ (R-1, C-1) satisfying the conditions
    if max1 >= min1 and max2 >= min2 and max1 >= 0 and min1 <= R + C - 2 and max2 >= 1 - C and min2 <= R - 1:
        i, j = 0, max1
        while i < R and j >= 0:
            if j < C and min2 <= i - j and i - j <= max2:
                return True
            i += 1
            j -= 1
        i, j = 0, min1
        while i < R and j >= 0:
            if j < C and min2 <= i - j and i - j <= max2:
                return True
            i += 1
            j -= 1

    return False

T = int(input())
for t in range(T):
    [R, C] = [int(n) for n in input().split()]
    offices = []
    dist = [[INF] * C for _ in range(R)]
    for i in range(R):
        for j, c in enumerate(input()):
            if c == '1':
                dist[i][j] = 0
                offices.append((i, j))

    # Use BFS to find the distance of all squares
    square_dist = [] # square_dist[i]: list of squares which has dist i
    queue = offices.copy()
    while queue:
        square_dist.append(queue)
        next_queue = []
        for (i, j) in queue:
            if i != 0 and dist[i - 1][j] == INF:
                dist[i - 1][j] = dist[i][j] + 1
                next_queue.append((i - 1, j))
            if i != R - 1 and dist[i + 1][j] == INF:
                dist[i + 1][j] = dist[i][j] + 1
                next_queue.append((i + 1, j))
            if j != 0 and dist[i][j - 1] == INF:
                dist[i][j - 1] = dist[i][j] + 1
                next_queue.append((i, j - 1))
            if j != C - 1 and dist[i][j + 1] == INF:
                dist[i][j + 1] = dist[i][j] + 1
                next_queue.append((i, j + 1))
        queue = next_queue

    # for i in range(R):
    #     print(dist[i])
    # for i, list in enumerate(square_dist):
    #     print(i, list)

    l, r = 0, len(square_dist) - 1
    ans = -1
    while l <= r:
        mid = (l + r) // 2
        # print(l, r, mid, exist_valid_office(mid))
        if exist_valid_office(mid):
            ans = mid
            r = mid - 1 # keep search [l, mid - 1] for more left target
        else:
            l = mid + 1

    if ans == -1:
    # All k return False, cannot find location for any better new office, so keep original max delivery distance
        print(f"Case #{t + 1}: {len(square_dist) - 1}")
    else:
        print(f"Case #{t + 1}: {ans}")
