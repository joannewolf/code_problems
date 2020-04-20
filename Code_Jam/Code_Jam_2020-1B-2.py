# https://codingcompetitions.withgoogle.com/codejam/round/000000000019fef2/00000000002d5b63

import sys
import random

MAX = 1000000000
MIN = -1000000000

class DoneBreak(Exception):
    pass

def check(x, y):
    assert type(x) is int and type(y) is int
    assert MIN <= x <= MAX and MIN <= y <= MAX
    print "{} {}".format(x, y)
    sys.stdout.flush()
    result = raw_input()
    if result == 'CENTER':
        raise DoneBreak
    else:
        return (result == 'HIT')

T, A, B = [int(n) for n in raw_input().split(' ')]
for t in xrange(T):
    try: 
        # get (x0, y0) in dartboard
        # at least around 1/4 of chance, cuz for case #3 Rmin = 10^9 / 2
        while True:
            x0 = random.randint(MIN, MAX)
            y0 = random.randint(MIN, MAX)
            if check(x0, y0):
                break

        # do binary search find (x1, y1) on (x0, y0)'s right side and close to edge
        bmin = x0
        bmax = MAX + 1
        y1 = y0
        while bmin < bmax:
            bmid = (bmin + bmax) / 2
            if check(bmid, y1):
                bmin = bmid + 1
            else:
                bmax = bmid
        x1 = max(x0, bmin - 1)

        # do binary search find (x2, y2a) on (x1, y1)'s up side and close to edge
        x2 = x1
        bmin = y1
        bmax = MAX + 1
        while bmin < bmax:
            bmid = (bmin + bmax) / 2
            if check(x2, bmid):
                bmin = bmid + 1
            else:
                bmax = bmid
        y2a = max(y1, bmin - 1)

        # do binary search find (x2, y2b) on (x1, y1)'s down side and close to edge
        bmin = MIN
        bmax = y1
        while bmin < bmax:
            bmid = (bmin + bmax) / 2
            if check(x2, bmid):
                bmax = bmid
            else:
                bmin = bmid + 1
        y2b = min(y1, bmin)

        assert y2b <= y2a

        # do binary search find (x3a, y2a) on (x2, y2a)'s left side and close to edge
        bmin = MIN
        bmax = x2
        while bmin < bmax:
            bmid = (bmin + bmax) / 2
            if check(bmid, y2a):
                bmax = bmid
            else:
                bmin = bmid + 1
        x3a = min(x2, bmin)

        # do binary search find (x3b, y2b) on (x2, y2b)'s left side and close to edge
        bmin = MIN
        bmax = x2
        while bmin < bmax:
            bmid = (bmin + bmax) / 2
            if check(bmid, y2b):
                bmax = bmid
            else:
                bmin = bmid + 1
        x3b = min(x2, bmin)

        # so far (x2, y2a), (x2, y2b), (x3a, y2a), (x3b, y2b) is a rectangle closely inscribed in the circle
        # circle center should be close to the rectangle center, check all points in 7 * 7 square around rectangle center for covering calculation error
        xca = (x2 + x3a) / 2
        xcb = (x2 + x3b) / 2
        yc = (y2a + y2b) / 2
        for center_x in range(min(xca, xcb) - 3, max(xca,xcb) + 3):
            for center_y in range(yc - 3, yc + 3):
                check(center_x, center_y)

    except DoneBreak:
        pass