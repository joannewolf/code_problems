# Square Dance
# https://codingcompetitions.withgoogle.com/codejam/round/000000000019fd74/00000000002b1355
# with optimization, O(R*C)
# only check the neighbor of the eliminated in the next round -> at most O(4*R*C checks) = O(R*C)
# for each check, use array to records neighbor -> O(1)

T = int(raw_input())
for t in xrange(T):
    R, C = [int(n) for n in raw_input().split(' ')]
    skills = []
    for i in xrange(R):
        skills.append([int(n) for n in raw_input().split(' ')])

    to_be_checked = set()
    left_neighbor_column = [[-1] * C for i in xrange(R)]
    right_neighbor_column = [[-1] * C for i in xrange(R)]
    up_neighbor_row = [[-1] * C for i in xrange(R)]
    down_neighbor_row = [[-1] * C for i in xrange(R)]
    # initializing
    for i in xrange(R):
        for j in xrange(C):
            to_be_checked.add((i, j))
            if j != 0:
                left_neighbor_column[i][j] = j - 1
            if j != C - 1:
                right_neighbor_column[i][j] = j + 1
            if i != 0:
                up_neighbor_row[i][j] = i - 1
            if i != R - 1:
                down_neighbor_row[i][j] = i + 1

    ans = 0
    while to_be_checked:
        eliminated = []
        neighbor_of_eliminated = set()
        ans += sum([sum(x) for x in skills])
        for (i, j) in to_be_checked:
            if skills[i][j] != 0:
                neighbor_count = 0
                neighbor_sum = 0
                if left_neighbor_column[i][j] != -1 and skills[i][left_neighbor_column[i][j]] != 0:
                    neighbor_count += 1
                    neighbor_sum += skills[i][left_neighbor_column[i][j]]
                if right_neighbor_column[i][j] != -1 and skills[i][right_neighbor_column[i][j]] != 0:
                    neighbor_count += 1
                    neighbor_sum += skills[i][right_neighbor_column[i][j]]
                if up_neighbor_row[i][j] != -1 and skills[up_neighbor_row[i][j]][j] != 0:
                    neighbor_count += 1
                    neighbor_sum += skills[up_neighbor_row[i][j]][j]
                if down_neighbor_row[i][j] != -1 and skills[down_neighbor_row[i][j]][j] != 0:
                    neighbor_count += 1
                    neighbor_sum += skills[down_neighbor_row[i][j]][j]
                # if Sij is gonna be eliminated, add its neighbors to the check list for next round
                # print "i, j", i, j, "neighbor_sum", neighbor_sum, "neighbor_count", neighbor_count
                if neighbor_count > 0 and skills[i][j] < neighbor_sum / float(neighbor_count):
                    eliminated.append((i, j))
                    if left_neighbor_column[i][j] != -1:
                        neighbor_of_eliminated.add((i, left_neighbor_column[i][j]))
                    if right_neighbor_column[i][j] != -1:
                        neighbor_of_eliminated.add((i, right_neighbor_column[i][j]))
                    if up_neighbor_row[i][j] != -1:
                        neighbor_of_eliminated.add((up_neighbor_row[i][j], j))
                    if down_neighbor_row[i][j] != -1:
                        neighbor_of_eliminated.add((down_neighbor_row[i][j], j))
        # print "eliminated", eliminated
        # eliminate competitors
        for (i, j) in eliminated:
            skills[i][j] = 0
            # the new right neighbor of Sij's left neighbor will be Sij's right neighbor
            if left_neighbor_column[i][j] != -1:
                right_neighbor_column[i][left_neighbor_column[i][j]] = right_neighbor_column[i][j]
            # the new left neighbor of Sij's right neighbor will be Sij's left neighbor
            if right_neighbor_column[i][j] != -1:
                left_neighbor_column[i][right_neighbor_column[i][j]] = left_neighbor_column[i][j]
            # the new up neighbor of Sij's down neighbor will be Sij's up neighbor
            if down_neighbor_row[i][j] != -1:
                up_neighbor_row[down_neighbor_row[i][j]][j] = up_neighbor_row[i][j]
            # the new down neighbor of Sij's up neighbor will be Sij's down neighbor
            if up_neighbor_row[i][j] != -1:
                down_neighbor_row[up_neighbor_row[i][j]][j] = down_neighbor_row[i][j]
            if (i, j) in neighbor_of_eliminated:
                neighbor_of_eliminated.remove((i, j))
        to_be_checked = neighbor_of_eliminated

    print "Case #{}: {}".format(t + 1, ans)