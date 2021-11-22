# Oversized Pancake Choppers
# https://codingcompetitions.withgoogle.com/codejam/round/000000000019fef4/00000000003172d1
# O(D * N^2)
# find slice size that can use as much slices fully as possible; for every full slice we use, we can save one cut

def reduce_fraction(x, y):
    temp_x = max(x, y)
    temp_y = min(x, y)
    while temp_y:
        temp_x, temp_y = temp_y, temp_x % temp_y
    return x / temp_x, y / temp_x

T = int(raw_input())
for t in xrange(T):
    N, D = [int(n) for n in raw_input().split(' ')]
    slices = [int(n) for n in raw_input().split(' ')]
    slices.sort()

    # all possible slice size = Ai / c, i = 1~N, c = 1~D -> O(N * D)
    slice_sizes = {} # (x, y) -> (f, s): with slice size x / y, there's f fully-used slices and produce s slices
    for A in slices:
        for c in range(1, D + 1):
            x, y = reduce_fraction(A, c)
            if (x, y) not in slice_sizes:
                slice_sizes[(x, y)] = (1, c)
            else:
                if c + slice_sizes[(x, y)][1] > D:
                    slice_sizes[(x, y)] = (slice_sizes[(x, y)][0], D)
                else:
                    slice_sizes[(x, y)] = (slice_sizes[(x, y)][0] + 1, slice_sizes[(x, y)][1] + c)

    ans = D - 1
    for s in slice_sizes:
        # the slice size is valid if sum(floor(Ai / size)) >= D for i = 1~N -> O(N)
        total_slices = 0
        for i in slices:
            total_slices += i * s[1] / s[0]
        if total_slices >= D:
            ans = min(ans, D - slice_sizes[s][0])

    print "Case #{}: {}".format(t + 1, ans)