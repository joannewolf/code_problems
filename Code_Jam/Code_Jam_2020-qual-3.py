# https://codingcompetitions.withgoogle.com/codejam/round/000000000019fd27/000000000020bdf9

T = raw_input()
for t in xrange(int(T)):
    N = int(raw_input())
    activities = []
    for n in xrange(N):
        # (index, start_time, end_time)
        activities.append(tuple([n] + [int(a) for a in raw_input().split(' ')]))
    # sort by start_time
    activities.sort(key = lambda x: x[1])

    endTimeC = -1
    endTimeJ = -1
    ans = ['X'] * N

    for activity in activities:
        if endTimeC <= activity[1]:
            endTimeC = activity[2]
            ans[activity[0]] = 'C'
        elif endTimeJ <= activity[1]:
            endTimeJ = activity[2]
            ans[activity[0]] = 'J'
        else:
            ans = "IMPOSSIBLE"
            break

    print "Case #{}: {}".format(t + 1, "".join(ans))