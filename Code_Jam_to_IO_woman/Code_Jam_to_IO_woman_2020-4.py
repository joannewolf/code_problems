# https://codingcompetitions.withgoogle.com/codejamio/round/000000000019ff03/00000000001b5e89
# each simple quadrilateral p1p2p3p4 can be divided into 2 triangles by p1p3 diagonal, p2 and p4 has to be on the different side of p1p3 line
# O(N^2) choose all combinations of p1 and p3, then O(N) calculate the distance of all other points to p1p3 line and choose minimum on both side -> total O(N^3)

import math

T = int(raw_input())
for t in xrange(int(T)):
    N = int(raw_input())
    points = []
    for n in xrange(N):
        points.append([int(x) for x in raw_input().split(' ')])

    ans = 10 ** 19
    for i in xrange(N):
        for j in xrange(i + 1, N):
            left_min = -10 ** 19
            right_min = 10 ** 19
            for k in xrange(N):
                if k != i and k != j:
                    # given 3 points' coordinator of triangle, (xi, yi), (xj, yj), (xk, yk)
                    # area = 1/2(xi*yj + xj*yk + xk*yi - xj*yi - xk*yj - xi*yk)
                    # area < 0 means 3 points in clockwise order, area > 0 means 3 points in counterclockwise order
                    coin = (points[i][0] * points[j][1] + points[j][0] * points[k][1] + points[k][0] * points[i][1]
                           - points[j][0] * points[i][1] - points[k][0] * points[j][1] - points[i][0] * points[k][1])
                    if coin < 0:
                        left_min = max(left_min, coin)
                    elif coin > 0:
                        right_min = min(right_min, coin)
            ans = min(ans, (-left_min + right_min))

    print "Case #{}: {}".format(t + 1, ans)