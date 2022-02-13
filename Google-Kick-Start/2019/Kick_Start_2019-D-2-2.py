# Latest Guests
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000051061/0000000000161427
# Sliding window, O(N)

T = int(input())
for t in range(T):
    [N, G, M] = [int(n) for n in input().split()]
    clockwise = [[] for i in range(N)]
    anticlockwise = [[] for i in range(N)]
    for i in range(G):
        [H, dir] = input().split()
        if dir == 'C':
            clockwise[int(H) - 1].append(i)
        else:
            anticlockwise[int(H) - 1].append(i)
    index_c = []
    index_a = []
    for i in range(N):
        if clockwise[i]:
            index_c.append(i)
        if anticlockwise[i]:
            index_a.append(i)
    # print(clockwise)
    # print(anticlockwise)
    # print(index_c)
    # print(index_a)

    if M > N:
        M = M % N + N

    # For each guest group, find how many consulate's latest guest is them
    latest_c = [-1] * N
    latest_a = [-1] * N
    for i in range(len(index_c) - 1, -1, -1):
        end = (index_c[i] + M) % N
        start = (index_c[i - 1] + M) % N
        if start == end: # When there's only one guest group
            covered_len = M + 1
        else:
            covered_len = min(M + 1, (end - start + N) % N)
        for j in range(end, end - covered_len, -1):
            latest_c[(j + N) % N] = index_c[i]

    for i in range(-1, len(index_a) - 1):
        end = (index_a[i] - M + 2 * N) % N
        start = (index_a[i + 1] - M + 2 * N) % N
        if start == end: # When there's only one guest group
            covered_len = M + 1
        else:
            covered_len = min(M + 1, (start - end + N) % N)
        for j in range(end, end + covered_len):
            latest_a[j % N] = index_a[i]
    # print(latest_c)
    # print(latest_a)

    # For each consulate, we've got the latest clockwise and anticlockwise guests
    # Now decide which one is later and that's the latest guests of that consulate
    count_c = [0] * N
    count_a = [0] * N
    for i in range(N):
        if latest_c[i] == -1 and latest_a[i] == -1:
        # No guest from clockwise and anticlockwise pass this consulate
            continue
        elif latest_c[i] == -1:
            count_a[latest_a[i]] += 1
        elif latest_a[i] == -1:
            count_c[latest_c[i]] += 1
        else:
            time_c = (i - latest_c[i] + N) % N
            time_a = (latest_a[i] - i + N) % N
            if M >= N:
                # It can be reached at second round
                if time_c <= M % N:
                    time_c += N
                if time_a <= M % N:
                    time_a += N

            if time_c > time_a:
                count_c[latest_c[i]] += 1
            elif time_a > time_c:
                count_a[latest_a[i]] += 1
            else:
                count_c[latest_c[i]] += 1
                count_a[latest_a[i]] += 1
    # print(count_c)
    # print(count_a)

    ans = [0] * G
    for i in range(N):
        for guest in clockwise[i]:
            ans[guest] = count_c[i]
        for guest in anticlockwise[i]:
            ans[guest] = count_a[i]
    print(f"Case #{t + 1}: {' '.join([str(n) for n in ans])}")
