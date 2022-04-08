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
MOD = pow(10, 9) + 7
def my_pow(a, b):
    result = 1
    while b != 0:
        if b % 2 == 1:
            result = result * a % MOD
        a = a * a % MOD
        b //= 2
    return result

##################################################
# To form a valid polygon
def is_good_polygon(edges: list):
    if len(edges) < 3:
        return False
    else:
        # In order to form a polygon, sum of all other edges > max edge
        return sum(edges) - max(edges) > max(edges)

##################################################
# Modular inverse, (a * x) % m = 1
# (b / a) % m = (b * x) % m
def modInverse1(a, m):
    for x in range(1, m):
        if (((a%m) * (x%m)) % m == 1):
            return x
    return -1

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