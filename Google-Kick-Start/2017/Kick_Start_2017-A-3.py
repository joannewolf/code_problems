# Two Cubes
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000201c97/0000000000201bff
# Ref: https://tandy123.github.io/2017/06/16/kickstart-2017-roundA/
# O(NlogM), M is the largest size of space

MAX_INT = 3 * pow(10, 8)
MIN_INT = -3 * pow(10, 8)

def check(min_x1, max_x1, min_y1, max_y1, min_z1, max_z1):
    length = max_x1 - min_x1
    not_bounded = set()
    for i in range(N):
        (x, y, z, r) = stars[i]
        if not (x - r >= min_x1 and x + r <= max_x1 and y - r >= min_y1 and y + r <= max_y1 and z - r >= min_z1 and z + r <= max_z1):
            not_bounded.add(i)

    max_x2 = MIN_INT
    min_x2 = MAX_INT
    max_y2 = MIN_INT
    min_y2 = MAX_INT
    max_z2 = MIN_INT
    min_z2 = MAX_INT
    for i in not_bounded:
        (x, y, z, r) = stars[i]
        max_x2 = max(max_x2, x + r)
        min_x2 = min(min_x2, x - r)
        max_y2 = max(max_y2, y + r)
        min_y2 = min(min_y2, y - r)
        max_z2 = max(max_z2, z + r)
        min_z2 = min(min_z2, z - r)

    return (max_x2 - min_x2) <= length and (max_y2 - min_y2) <= length and (max_z2 - min_z2) <= length

T = int(input())
for t in range(T):
    N = int(input())
    stars = []
    for _ in range(N):
        stars.append([int(x) for x in input().split()])

    # First find the bounding box for all stars
    max_x = MIN_INT
    min_x = MAX_INT
    max_y = MIN_INT
    min_y = MAX_INT
    max_z = MIN_INT
    min_z = MAX_INT
    for (x, y, z, r) in stars:
        max_x = max(max_x, x + r)
        min_x = min(min_x, x - r)
        max_y = max(max_y, y + r)
        min_y = min(min_y, y - r)
        max_z = max(max_z, z + r)
        min_z = min(min_z, z - r)
    # print(max_x, min_x, max_y, min_y, max_z, min_z)

    # Then put one box in every corner of the bounding box, it can contain some stars
    # For the other stars which cannot be bounded by first box, check whether they can be bounded by another box with same edge length
    # Use binary search to find the smallest length which func return true
    l = 1
    r = max(max_x - min_x, max_y - min_y, max_z - min_z)
    ans = -1
    while l <= r:
        mid = (l + r) // 2
        ok = (check(min_x, min_x + mid, min_y, min_y + mid, min_z, min_z + mid) or
            check(min_x, min_x + mid, min_y, min_y + mid, max_z - mid, max_z) or
            check(min_x, min_x + mid, max_y - mid, max_y, min_z, min_z + mid) or
            check(min_x, min_x + mid, max_y - mid, max_y, max_z - mid, max_z) or
            check(max_x - mid, max_x, min_y, min_y + mid, min_z, min_z + mid) or
            check(max_x - mid, max_x, min_y, min_y + mid, max_z - mid, max_z) or
            check(max_x - mid, max_x, max_y - mid, max_y, min_z, min_z + mid) or
            check(max_x - mid, max_x, max_y - mid, max_y, max_z - mid, max_z)
        )
        # print("l", l, "r", r, "mid", mid, ok)
        if ok:
            ans = mid
            r = mid - 1 # keep search [L, mid - 1] for more left target
        else:
            l = mid + 1
    
    print(f"Case #{t + 1}: {ans}")
