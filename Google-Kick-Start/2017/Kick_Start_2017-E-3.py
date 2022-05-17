# Blackhole
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000201bfe/0000000000201b78
# Ref: https://github.com/kamyu104/GoogleKickStart-2017/blob/main/Round%20E/blackhole.py
# The problem can be simplified to 2-D problem, since there always exists a plane in 3-D containing three blackhole points
# Key idea: Let 3 blackhole be X, Y, Z, and 3 circle be A, B, C, A connected to B, B connected to C, A not necessarily connected to C
# There's only two possible optimal types
# Type 1: one point in each circle, there are 3 possibilities, let K be the center of circle B
#   dist(K, Y) <= R so Y must be inside B; dist(K, X) <= 3R, dist(K, Z) <= 3R so A and C must be connected to B
#   <-> Find intersection of circles center at Y with radius R, center at X, Z with radius 3R
# Type 2: two points in circle A, one points in circle C, there are 3 possibilities, let K be the center of circle A
#   dist(K, X) <= R, dist(K, Y) <= R so X and Y must be inside A; dist(K, Z) <= 5R, so A and C must be connected via B
#   <-> Find intersection of circles center at X, Y with radius R, center at Z with radius 5R
# Use binary search to find the minimum radius which satisfy type 1 or 2

import math

ERROR = pow(10, -10)
INF = float("inf")

def dist(a, b):
    return length(vector(a, b))

def vector(a, b):
    return [a[i]-b[i] for i in range(len(a))]

def inner_product(a, b):
    return sum(a[i] * b[i] for i in range(len(a)))

def outer_product(a, b):
    return [a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0]]

def length(a): # Given a vector
    return sum(x**2 for x in a)**0.5

def normalize(a): # Result vector length == 1
    l = length(a)
    return [x / l for x in a] if l else a

def angle(a, b, norm):
    # math.atan2(y, x) returns the arc tangent of y/x, in radians. Where x and y are the coordinates of a point (x,y)
    return math.atan2(inner_product(outer_product(a, b), norm)/length(norm), inner_product(a, b))

def normal_vector(a, b):
    result = outer_product(a, b)
    # If result == [0, 0, 0], means a and b are parallel
    if result != [0, 0, 0]:
        return result
    if 0 in a:
        j = a.index(0)
        return [int(i == j) for i in range(3)]  # Give a default normal vector of plane
    return [a[1], -a[0], 0]  # Give a default normal vector of plane

def matrix_multi(A, B):
    assert(len(A[0]) == len(B))
    result = [[0.0 for _ in range(len(B[0]))] for _ in range(len(A))]
    for i in range(len(A)):
        for k in range(len(A[0])):
            for j in range(len(B[0])):
                result[i][j] += A[i][k] * B[k][j]
    return result

def rotate_u(matrix, cosx, sinx, u):
    Ru = [[cosx+u[0]*u[0]*(1-cosx)     , u[1]*u[0]*(1-cosx)+u[2]*sinx, u[2]*u[0]*(1-cosx)-u[1]*sinx],
          [u[0]*u[1]*(1-cosx)-u[2]*sinx, cosx+u[1]*u[1]*(1-cosx)     , u[2]*u[1]*(1-cosx)+u[0]*sinx],
          [u[0]*u[2]*(1-cosx)+u[1]*sinx, u[1]*u[2]*(1-cosx)-u[0]*sinx, cosx+u[2]*u[2]*(1-cosx)     ]]
    return matrix_multi(matrix, Ru)

def rotate_to_2D(points):
    v = normalize(normal_vector(vector(points[0], points[1]), vector(points[0], points[2])))
    # v: the normal vector of 3 blackhole points plane
    u = normalize(normal_vector(v, [0, 0, 1]))
    # u: the normal vector of v and z-axis
    theta = angle(v, [0, 0, 1], u)
    return [[x, y] for x, y, _ in rotate_u(points, math.cos(theta), math.sin(theta), u)]

def circle_intersect(a, b):
    # Let a always be smaller circle
    if a[1] > b[1]:
        a, b = b, a
    X1, Y1 = a[0]
    X2, Y2 = b[0]
    R1, R2 = a[1], b[1]
    Dx = X2-X1
    Dy = Y2-Y1
    D = (Dx**2 + Dy**2)**0.5 # Distance of the centers of two circles
    if D > R1+R2: # Disjoint circles
        return 0, None  
    elif D > R2-R1:
        chord_dist = (R1**2 - R2**2 + D**2)/(2*D)  # Cover two cases R1^2+D^2 >= R2^2, R1^2+D^2 < R2^2
        assert((R1**2 - chord_dist**2) >= -ERROR)  # May have some small error
        half_chord_len = max(R1**2 - chord_dist**2, 0.0)**0.5
        chord_mid_x = X1 + (chord_dist*Dx)/D
        chord_mid_y = Y1 + (chord_dist*Dy)/D
        I1 = (chord_mid_x + (half_chord_len*Dy)/D,
              chord_mid_y - (half_chord_len*Dx)/D)
        I2 = (chord_mid_x - (half_chord_len*Dy)/D,
              chord_mid_y + (half_chord_len*Dx)/D)
        return 2, (I1, I2)  # Two points (include duplicated points)
    else: # Infinite points, circle b fully cover circle a
        return float("inf"), a

def circle_contain(a, p):
    return (p[0] - a[0][0]) ** 2 + (p[1] - a[0][1]) ** 2 <= a[1] ** 2

def intersect(a, b, c):
    num, res = circle_intersect(a, b)
    if num == 0: # No intersect
        return False
    if num == 2: # Intersect with 1 or 2 points
        if circle_contain(c, res[0]) or circle_contain(c, res[1]):
            return True
        return False
    if num == INF: # One circle fully inside another circle
        # Check if smaller circle intersect with third circle
        return circle_intersect(res, c)[0] != 0
    return False

def is_overlapped(a, b, c):
    return intersect(a, b, c) or intersect(b, c, a) or intersect(c, a, b)

def check_types(a, b, c, r):
    return is_overlapped((a, r), (b, 3*r), (c, 3*r)) or is_overlapped((a, 5*r), (b, r), (c, r))

def check(a, b, c, r):
    return check_types(a, b, c, r) or check_types(b, c, a, r) or check_types(c, a, b, r)

T = int(input())
for t in range(T):
    blackhole = []
    for _ in range(3):
        (x, y, z) = [int(x) for x in input().split()]
        blackhole.append((x, y, z))

    a, b, c = rotate_to_2D(blackhole) # a, b, c become 2D points
    max_dist = max(dist(a, b), dist(b, c), dist(a, c))
    l = max_dist / 6
    r = max_dist
    while r - l > ERROR:
        mid = (l + r) / 2
        if check(a, b, c, mid):
            r = mid
        else:
            l = mid

    print(f"Case #{t + 1}: {l}")
