# Ants on a Stick
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000008cb4d1/0000000000b209bc
# Ants bouncing off can be seen as ants passing by each other but exchanging ID card
# Any ant which initially facing right, will exchange ID card with all ants on its right side and facing left
# Collect all exchanging event, sort by happening time, and track the ID
# O(N^2logN), MLE on test set 3

T = int(input())
for t in range(T):
    [N, L] = [int(x) for x in input().split()]
    ants = []
    for i in range(N):
        [p, d] = [int(x) for x in input().split()]
        ants.append((i, p, d))
    ants.sort(key=lambda x: x[1]) # Sort by initial position

    # Track the ID card of ants based on initial index
    index = list(range(1, N+1))
    events = []
    for i in range(N):
        if ants[i][2] == 1:
            # Only need to check the ants on the right side and facing left
            for j in range(i+1, N):
                if ants[j][2] == 0:
                    events.append(((ants[j][1] - ants[i][1]) / 2, ants[i][0], ants[j][0]))
                    # abs(P1 - P2) / 2 is the time that ID exchange happening
    events.sort()
    # print(events)

    for e in events:
        i, j = e[1], e[2]
        # print(i, j, index)
        index[i], index[j] = index[j], index[i]
    # print(index)

    # Find the drop order based on initial position and direction
    drop_time = []
    for i in range(N):
        (idx, p, d) = ants[i]
        if d == 0:
            drop_time.append((p, index[idx]))
        else:
            drop_time.append((L - p, index[idx]))
    drop_time.sort()
    ans = [x[1] for x in drop_time]

    print(f"Case #{t + 1}: {' '.join(map(str, ans))}")
