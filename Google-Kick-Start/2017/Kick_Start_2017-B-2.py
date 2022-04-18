# Center
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000201d27/0000000000201c01
# Key idea1: Use ternary search to find the optimal point in the middle, big...small...big
# Key idea2: Convert Chebyshev distance to Manhattan distance: (x, y) -> ((x+y)/2, (x-y)/2), so it becomes finding min SUM{abs(x-xi) + abs(y-yi)}

MAX_DBL = 1000.0
MIN_DBL = -1000.0
ERROR = pow(10, -6)

# flag: True for x-axis, False for y-axis
def dist(p: float, flag: bool):
    res = 0
    if flag:
        for i in range(N):
            res += abs(p - points[i][0]) * points[i][2]
    else:
        for i in range(N):
            res += abs(p - points[i][1]) * points[i][2]
    return res

def search(l: float, r: float, flag: bool):
    ans = min(dist(l, flag), dist(r, flag))
    while r - l > ERROR:
        mid1 = (l + l + r) / 3
        mid2 = (l + r + r) / 3
        # print("l", l, "r", r, mid1, mid2)
        res1 = dist(mid1, flag)
        res2 = dist(mid2, flag)
        if res1 < res2: # mid1 is closer to the middle smallest point
            r = mid2
        else:
            l = mid1
        ans = min(ans, res1, res2)

    return ans

T = int(input())
for t in range(T):
    N = int(input())
    points = []
    for _ in range(N):
        (x, y, w) = [float(x) for x in input().split()]
        points.append(((x+y)/2, (x-y)/2, w))
    # print(points)

    max_x = MIN_DBL
    min_x = MAX_DBL
    max_y = MIN_DBL
    min_y = MAX_DBL
    for i in range(N):
        (x, y, w) = points[i]
        max_x = max(max_x, x)
        min_x = min(min_x, x)
        max_y = max(max_y, y)
        min_y = min(min_y, y)
    # print(min_x, max_x, min_y, max_y)

    ans = search(min_x, max_x, True) + search(min_y, max_y, False)
    print(f"Case #{t + 1}: {ans}")
