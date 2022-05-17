import math

# GCD using iteration
def gcd(a, b):
    while (a % b) > 0:
        a, b = b, a % b
    return b

# GCD using recursion
def gcd2(a, b):
    if b == 0:
        return a
    else:
        return gcd2(b, a % b)

# Extended Euclidean algorithm, find integer s, t such that as + bt = r = gcd(a, b)
# https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm
def ext_gcd(a, b):
    old_s, s = 1, 0
    old_t, t = 0, 1
    old_r, r = a, b
    while(r!=0):
        q = old_r // r
        old_r, r = r, old_r-q*r # a % b
        old_s, s = s, old_s-q*s
        old_t, t = t, old_t-q*t
    print(f"({old_s}*{a}) + ({old_t}*{b}) = {old_r}")
    return old_s, old_t, old_r

# print(gcd(10, 12))
# print(gcd(12, 9))
# print(gcd2(10, 12))
# print(gcd2(12, 9))
# print(ext_gcd(12, 9))
# print(ext_gcd(3, 0))
# print(ext_gcd(9, 12))
# print(ext_gcd(0, 3))

##################################################
# To form a valid polygon
def is_good_polygon(edges: list):
    if len(edges) < 3:
        return False
    else:
        # In order to form a polygon, sum of all other edges > max edge
        return sum(edges) - max(edges) > max(edges)

##################################################
# (a + b) % p = (a % p + b % p) % p
# (a – b) % p = (a % p – b % p) % p
# (a * b) % p = (a % p * b % p) % p
# Modular inverse, if (a * x) % m = 1, then (b / a) % m = (b * x) % m

MOD = pow(10, 9) + 7
INV3 = (MOD + 1) // 3

def modInverse1(a, m):
    for x in range(1, m):
        if (((a%m) * (x%m)) % m == 1):
            return x
    return -1

# Extended Euclidean algorithm
def modInverse2(a, m):
    m0 = m
    y = 0
    x = 1
 
    if (m == 1):
        return 0
 
    while (a > 1):
        q = a // m # quotient
        t = m

        # m is remainder now, process, same as Euclid's algo
        m = a % m
        a = t
        t = y
 
        # Update x and y
        y = x - q * y
        x = t

    # Make x positive
    if (x < 0):
        x = x + m0

    return x

def my_pow(a, b):
    ans = 1
    while b:
        if b & 1:
            ans = ans * a % MOD
        b >>= 1
        a = a * a % MOD
    return ans

N = 10
fac = [1] * (N + 1)
rfac = [1] * (N + 1)
inv = [1] * (N + 1)
for i in range(1, N + 1):
    fac[i] = fac[i - 1] * i % MOD
rfac[N] = my_pow(fac[N], MOD - 2)
for i in range(N - 1, 0, -1):
    rfac[i] = rfac[i + 1] * (i + 1) % MOD
for i in range(1, N):
    inv[i] = rfac[i] * fac[i-1] % MOD

# print(INV3) # 333333336
# print(modInverse2(3, MOD)) # 333333336
# print(pow(3, MOD - 2)) # 333333336
# print(fac[3], rfac[3], fac[3] * rfac[3] % MOD)
# print(inv[3]) # 333333336
# print(inv[4], 4 * inv[4] % MOD)

##################################################
# Chebyshev distance: max(|x2-x1|, |y2-y1|)
# Manhattan distance: |x2-x1| + |y2-y1|
#   Chebyshev distance to Manhattan distance: (x, y) -> ((x+y)/2, (x-y)/2)
# Euclidean distance: sqrt((x2-x1)^2 + (y2-y1)^2)

##################################################
# Vector-related
def vector(a, b):
    return [a[i]-b[i] for i in range(len(a))]

def inner_product(a, b):
    return sum(a[i] * b[i] for i in range(len(a)))

def outer_product(a, b):
    return [a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0]]

def length(a): # Given a vector
    return sum(x**2 for x in a)**0.5

def normalized(a): # Result vector length == 1
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

# Given 3 points in 3-D world, convert it to 2-D points on their common plane
def rotate_3D_to_2D(points):
    v = normalized(normal_vector(vector(points[0], points[1]), vector(points[0], points[2])))
    # v: the normal vector of 3 points plane
    u = normalized(normal_vector(v, [0, 0, 1]))
    # u: the normal vector of v and z-axis
    theta = angle(v, [0, 0, 1], u)
    return [[x, y] for x, y, _ in rotate_u(points, math.cos(theta), math.sin(theta), u)]

# print(outer_product((1, 2, 3), (2, 4, 6))) # (0, 0, 0) means two vectors are parallel

##################################################
# http://paulbourke.net/geometry/circlesphere/ - Intersection of two circles
# a = ((x1, y1), r1); b = ((x2, y2), r2)
# return intersect_count, result
EPS = pow(10, -10)
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
        assert((R1**2 - chord_dist**2) >= -EPS)  # May have some small error
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
