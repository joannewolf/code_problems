# https://codingcompetitions.withgoogle.com/codejam/round/000000000019fef4/00000000003172d1
# O(D * N)
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
    # slice_sizes_dict: (x, y) -> [s_0, s_1, ..., s_n]
    # with slice size x / y, there are n slices that can be fully used and each produce s_i slices, and they are sorted
    slice_sizes_dict = {}
    for A in slices:
        for c in range(1, D + 1):
            x, y = reduce_fraction(A, c)
            if (x, y) not in slice_sizes_dict:
                slice_sizes_dict[(x, y)] = [c]
            else:
                slice_sizes_dict[(x, y)].append(c)

    # use binary search to find the max valid slice size
    # the slice size is valid if sum(floor(Ai / size)) >= D for i = 1~N -> O(N)
    slice_sizes = sorted(list(slice_sizes_dict.keys()), key=lambda k: k[0] / float(k[1]))
    smax = len(slice_sizes) - 1
    smin = 0
    while smin < smax:
        smid = (smin + smax + 1) / 2
        total_slices = 0
        for A in slices:
            total_slices += A * slice_sizes[smid][1] / slice_sizes[smid][0]
        if total_slices < D:
            smax = smid - 1
        else:
            smin = smid

    ans = D - 1
    for size in slice_sizes[0: smin + 1]:
        full_slices = 0
        total_slices = 0
        for s in slice_sizes_dict[size]:
            if total_slices + s <= D:
                full_slices += 1
                total_slices += s
            else:
                break
        ans = min(ans, D - full_slices)

    print "Case #{}: {}".format(t + 1, ans)