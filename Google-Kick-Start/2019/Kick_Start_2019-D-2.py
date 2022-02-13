# Latest Guests
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000051061/0000000000161427
# O(N^2), TLE on test set 2

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
    # print(clockwise)
    # print(anticlockwise)

    if M > N:
        M = M % N + N

    ans = [0] * G
    # For each consulate find the latest guests
    for i in range(N):
        # Check from M mins later, find if there are guests coming
        for m in range(M, -1, -1):
            guest = clockwise[(i - m + 2 * N) % N] + anticlockwise[(i + m) % N]
            if guest:
                for g in guest:
                    ans[g] += 1
                break

    print(f"Case #{t + 1}: {' '.join([str(n) for n in ans])}")
