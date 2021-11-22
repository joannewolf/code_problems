# Star Trappers
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435bae/0000000000888d45
# The minimum polygon must be triangle or quadrilateral (where target is on the intersection of diagonals)
# If target is in quadrilateral but not in intersection of diagonals, it definitely can reduce to some triangle which has smaller perimeter

import math

def sign(p1, p2, p3):
    return (p1[0] - p3[0]) * (p2[1] - p3[1]) - (p2[0] - p3[0]) * (p1[1] - p3[1])

def get_perimeter(points: list):
    result = 0
    N = len(points)
    for i in range(-1, N - 1):
        result += math.sqrt(pow(points[i][0] - points[i + 1][0], 2) + pow(points[i][1] - points[i + 1][1], 2))
    return result

MAX_INT = pow(10, 7)
T = int(input())
for t in range(T):
    N = int(input())
    stars = []
    for i in range(N):
        [x, y] = [int(n) for n in input().split()]
        stars.append((x, y))
    target = [int(n) for n in input().split()]

    target_on_lines = set()

    result = MAX_INT
    for i in range(N - 2):
        for j in range(i + 1, N - 1):
            for k in range(j + 1, N):
                d1 = sign(target, stars[i], stars[j])
                d2 = sign(target, stars[j], stars[k])
                d3 = sign(target, stars[k], stars[i])
                if d1 == 0:
                    target_on_lines.add((i, j))
                if d2 == 0:
                    target_on_lines.add((j, k))
                if d3 == 0:
                    target_on_lines.add((i, k))

                if (d1 < 0 and d2 < 0 and d3 < 0) or (d1 > 0 and d2 > 0 and d3 > 0):
                    # Target in triangle
                    perimeter = get_perimeter([stars[i], stars[j], stars[k]])
                    if perimeter < result:
                        result = perimeter

    target_on_lines = list(target_on_lines)
    if target_on_lines:
        M = len(target_on_lines)
        for i in range(M - 1):
            for j in range(i + 1, M):
                p1 = stars[target_on_lines[i][0]]
                p2 = stars[target_on_lines[j][0]]
                p3 = stars[target_on_lines[i][1]]
                p4 = stars[target_on_lines[j][1]]
                d1 = sign(target, p1, p2)
                d2 = sign(target, p2, p3)
                d3 = sign(target, p3, p4)
                d4 = sign(target, p4, p1)
                if (d1 < 0 and d2 < 0 and d3 < 0 and d4 < 0) or (d1 > 0 and d2 > 0 and d3 > 0 and d4 > 0):
                    # Target in quadrilateral
                    perimeter = get_perimeter([p1, p2, p3, p4])
                    if perimeter < result:
                        result = perimeter

    if result == MAX_INT:
        print(f"Case #{t + 1}: IMPOSSIBLE")
    else:
        print(f"Case #{t + 1}: {result}")
