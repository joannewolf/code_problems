# Combining Classes
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000051066/0000000000051007
# O(NlogN + QlogN)

T = int(input())
for t in range(T):
    [N, Q] = [int(x) for x in input().split()]
    [X1, X2, A1, B1, C1, M1] = [int(x) for x in input().split()]
    [Y1, Y2, A2, B2, C2, M2] = [int(x) for x in input().split()]
    [Z1, Z2, A3, B3, C3, M3] = [int(x) for x in input().split()]
    X = [X1, X2]
    Y = [Y1, Y2]
    starts = []
    ends = []
    quests = [Z1, Z2]
    for i in range(2, N):
        next_x = (X[-1] * A1 + X[-2] * B1 + C1) % M1
        X.append(next_x)
        next_y = (Y[-1] * A2 + Y[-2] * B2 + C2) % M2
        Y.append(next_y)
    for i in range(N):
        starts.append(min(X[i], Y[i]) + 1)
        ends.append(max(X[i], Y[i]) + 1)
    starts.sort()
    ends.sort()
    # print(starts)
    # print(ends)
    for i in range(2, Q):
        next_k = (quests[-1] * A3 + quests[-2] * B3 + C3) % M3
        quests.append(next_k)
    for i in range(Q):
        quests[i] += 1
    # print(quests)

    # List scores and their count
    score_now = -1
    score_count = 0
    # scores[i] = [l, r]: between l and r (inclusive), they are all having count[i]
    scores = []
    count = []
    flag_s = 0
    flag_e = 0
    while flag_s < N or flag_e < N:
        # print("flag_s", flag_s, "flag_e", flag_e, "score_now", score_now, "score_count", score_count)
        if flag_s == N or ends[flag_e] < starts[flag_s]:
            if score_now <= ends[flag_e]:
                if not scores or scores[-1][1] != score_now:
                    scores.append((score_now, ends[flag_e]))
                    count.append(score_count)
                score_now = ends[flag_e] + 1
            score_count -= 1
            flag_e += 1
        else:
            if score_count == 0:
                score_now = starts[flag_s]
                score_count = 1
            else:
                if score_now < starts[flag_s]:
                    scores.append((score_now, starts[flag_s] - 1))
                    count.append(score_count)
                score_now = starts[flag_s]
                score_count += 1
            flag_s += 1
        # print(scores)
        # print(count)
    # Since the requests are asking K-th highest score, we reverse the scores and count
    scores.reverse()
    count.reverse()

    # Add the prefix count => there are count[i] students having score <= scores[i][1]
    prefix_count = [0]
    N_scores = len(scores)
    for i in range(N_scores):
        prefix_count.append(prefix_count[-1] + count[i] * (scores[i][1] - scores[i][0] + 1))
    prefix_count.pop(0)
    # print(scores)
    # print(count)
    # print(prefix_count)

    ans = 0
    for i in range(Q):
        # Use binary search to find K-th highest score in which range, final L is min element index which >= target
        l, r = 0, N_scores - 1
        while l <= r:
            mid = (l + r) // 2
            if prefix_count[mid] < quests[i]:
                l = mid + 1
            else:
                r = mid - 1
        # print("K", quests[i], "l", l, "r", r)
        if l != N_scores:
            target = scores[l][0] + (prefix_count[l] - quests[i]) // count[l]
            # print("target", target)
            ans += (i + 1) * target

    print(f"Case #{t + 1}: {ans}")
