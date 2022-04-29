# Trash
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000201b77/0000000000201d23
# Ref: https://github.com/ckcz123/codejam/blob/master/kickstart/2017/RoundD/C.java

ERROR = pow(10, -10)

# Whether the parabola with given "a" is out of circle with center (x, y) and radius R
# The circle is adjusted s.t. the parabola's top point is at (0, 0), i.e. parabola equation is y = ax^2
def is_out_circle(a: float, x0: float, y0: float, R:float):
    # If a parabola is out of circle, for every point on parabola, it should satisfy (x - x0)^2 + (y - y0)^2 >= R^2
    # -> (x - x0)^2 + (ax^2 - y0)^2 >= R^2
    # -> f(x) = a^2x^4 + (-2ay0 + 1)x^2 -2x0x +(x0^2 + y0^2 - R^2) >= 0
    a4 = a * a
    a2 = -2 * a * y0 + 1
    a1 = -2 * x0
    a0 = x0 * x0 + y0 * y0 - R * R
    # -> Min point should be at f'(x) = 0
    # -> 4a4x^3 + 2a2x + a1 = 0
    b3 = 4 * a4
    b1 = 2 * a2
    b0 = a1
    l, r = -P/2, 0 # Enough to check left half of parabola
    while r - l > ERROR:
        mid = (l + r) / 2
        if b3 * mid * mid * mid + b1 * mid + b0 < 0:
            l = mid
        else:
            r = mid
    return (a4 * l * l * l * l + a2 * l * l + a1 * l + a0) >= 0

# Given radius R, check whether there's valid "a" for parabola
# Key idea: Convert the problem to: given obstacle circles with radius R and ceiling height H - R, whether there exists a parabola not touching the circles
# a <= 0, while a is smaller, the parabola is more curved and high
# In order to avoid the obstacle circle, it must pass above it or below it, then a's range must be > some a* or < some a**, see if there exists valid a
# The highest point of parabola is when x = P / 2 -> y = ax(x - P) = -P^2 * a / 4 <= H - R

# Circle equation: (x - X)^2 + (y - Y)^2 = R^2
# Parabola equation: y = ax(x - P)
def check(R: float):
    # 4(R-H)/P^2 <= a <= bound[i][0], bound[i][1] <= a <= 0
    min_a = 4 * (R - H) / (P * P)
    bound = [[0] * 2 for _ in range(N)]
    for i in range(N):
        (X, Y) = obstacle[i]
        _a = Y / X / (X - P) # The parabola which pass (X, Y), use this as start point to search up and down

        # Find lower bound, parabola pass above obstacle
        if X <= R: # The obstacle circle cross y-axis to negative-x field, parabola can never pass over it
            bound[i][0] = min_a - 1
        else:
            l, r = min_a - 1, _a
            while r - l > ERROR:
                mid = (l + r) / 2
                CX = P / 2
                CY = mid * CX * (CX - P)
                if is_out_circle(mid, X - CX, Y - CY, R):
                    # Parabola is out of circle, adjust it flatter
                    l = mid
                else:
                    r = mid
            bound[i][0] = l

        # Find upper bound, parabola pass below obstable
        if Y <= R: # The obstacle circle cross x-axis to negative-y field, parabola can never pass below it
            bound[i][1] = 1
        else:
            l, r = _a, 0
            while r - l > ERROR:
                mid = (l + r) / 2
                CX = P / 2
                CY = mid * CX * (CX - P)
                if is_out_circle(mid, X - CX, Y - CY, R):
                    # Parabola is out of circle, adjust it more curved
                    r = mid
                else:
                    l = mid
            bound[i][1] = l

    intervals = [[min_a, 0]]
    for (lower, upper) in bound:
        next = []
        for (l, r) in intervals:
            (new_l, new_r) = (l, r)
            new_r = min(r, lower)
            if new_l <= new_r + ERROR:
                next.append([new_l, new_r])
            (new_l, new_r) = (l, r)
            new_l = max(l, upper)
            if new_l <= new_r + ERROR:
                next.append([new_l, new_r])
        intervals = next
    # print(intervals)
    return bool(intervals)

T = int(input())
for t in range(T):
    [N, P, H] = [int(x) for x in input().split()]
    obstacle = []
    for _ in range(N):
        [x, y] = [int(x) for x in input().split()]
        if x >= P / 2:
            # Put all obstacles in the left half of parabola
            x  = P - x
        obstacle.append((x, y))

    # Use binary search to find the biggest radius which check return true
    ans = -1
    l, r = 0, H
    while r - l > ERROR:
        mid = (l + r) / 2
        # print("radius", "l", l, "r", r, "mid", mid)
        if check(mid):
            l = mid
        else:
            r = mid

    print(f"Case #{t + 1}: {l}")
