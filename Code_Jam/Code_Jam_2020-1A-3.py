# https://codingcompetitions.withgoogle.com/codejam/round/000000000019fd74/00000000002b1355
# brute-force O((R*C rounds) * (R*C*(R+C) checks per round))
T = int(raw_input())
for t in xrange(T):
    R, C = [int(n) for n in raw_input().split(' ')]
    skills = []
    for i in xrange(R):
        skills.append([int(n) for n in raw_input().split(' ')])

    ans = 0
    while True:
        eliminated = 0
        ans += sum([sum(c) for c in skills])
        for i in xrange(R):
            for j in xrange(C):
                if skills[i][j] != 0:
                    neighbor_sum = 0
                    neighbor_count = 0
                    # find right neighbor
                    for k in xrange(j + 1, C):
                        if skills[i][k] != 0:
                            neighbor_sum += abs(skills[i][k])
                            neighbor_count += 1
                            break
                    # find left neighbor
                    for k in xrange(j - 1, -1, -1):
                        if skills[i][k] != 0:
                            neighbor_sum += abs(skills[i][k])
                            neighbor_count += 1
                            break
                    # find down neighbor
                    for k in xrange(i + 1, R):
                        if skills[k][j] != 0:
                            neighbor_sum += abs(skills[k][j])
                            neighbor_count += 1
                            break
                    # find up neighbor
                    for k in xrange(i - 1, -1, -1):
                        if skills[k][j] != 0:
                            neighbor_sum += abs(skills[k][j])
                            neighbor_count += 1
                            break
                    # if competitor is gonna be eliminated, mark it as negative
                    if neighbor_count > 0 and skills[i][j] < neighbor_sum / float(neighbor_count):
                        skills[i][j] = -skills[i][j]
                        eliminated += 1
        # eliminate competitors
        for i in xrange(R):
            for j in xrange(C):
                if skills[i][j] < 0:
                    skills[i][j] = 0
        if eliminated == 0:
            break

    print "Case #{}: {}".format(t + 1, ans)