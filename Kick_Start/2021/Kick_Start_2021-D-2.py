# Cutting Intervals
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000004361e3/000000000082b933

T = int(input())
for t in range(T):
    [N, C] = [int(n) for n in input().split()]
    starts = []
    ends = []
    for i in range(N):
        [s, e] = [int(n) for n in input().split()]
        starts.append(s)
        ends.append(e)

    starts.sort()
    ends.sort()

    cuts = {} # key: # of overlap invertals, value: # of such cutting point
    overlap = 0
    flag = 2 # interval L >= 1, so smallest cut starts from 2
    index_s = 0
    index_e = 0
    while index_s < N or index_e < N:
        if index_s < N and flag > starts[index_s]:
            overlap += 1
            index_s += 1
        elif index_e < N and flag == ends[index_e]:
            overlap -= 1
            index_e += 1
        else:
            if index_s < N and index_e < N:
                next_flag = min(starts[index_s] + 1, ends[index_e])
            elif index_s < N:
                next_flag = starts[index_s] + 1
            else:
                next_flag = ends[index_e]
            # print("flag", flag, "index_s", index_s, "index_e", index_e, "next_flag", next_flag, "overlap", overlap)
            if overlap in cuts:
                cuts[overlap] += (next_flag - flag)
            else:
                cuts[overlap] = (next_flag - flag)
            flag = next_flag
            # print(cuts)

    result = N
    # Start cutting from the points with most overlap
    cuts = sorted(list(cuts.items()), reverse=True)
    for overlap, count in cuts:
        if C >= count:
            result += overlap * count
            C -= count
        else:
            result += overlap * C
            break

    print(f"Case #{t + 1}: {result}")
