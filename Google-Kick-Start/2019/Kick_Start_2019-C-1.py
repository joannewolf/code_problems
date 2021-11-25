# Wiggle Walk
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050ff2/0000000000150aac
# For each instruction, it takes O(logN) to find the interval, O(NlogN)

def insert_not_exist_new_square(intervals, new_val):
    l, r = 0, len(intervals) - 1
    while l <= r:
        mid = (l + r) // 2
        if intervals[mid][0] < new_val:
            l = mid + 1
        else:
            r = mid - 1
    # final l is the index for inserting
    insert_interval(intervals, l, new_val)

def insert_interval(intervals, new_pos, new_val):
    if new_pos != 0 and new_pos != len(intervals) and new_val == intervals[new_pos-1][1] + 1 and new_val == intervals[new_pos][0] - 1:
        intervals[new_pos-1:new_pos+1] = [[intervals[new_pos-1][0], intervals[new_pos][1]]]
    elif new_pos != 0 and new_val == intervals[new_pos-1][1] + 1:
        intervals[new_pos-1][1] += 1
    elif new_pos != len(intervals) and new_val == intervals[new_pos][0] - 1:
        intervals[new_pos][0] -= 1
    else:
        intervals.insert(new_pos, [new_val, new_val])

T = int(input())
for t in range(T):
    [N, R, C, Sr, Sc] = [int(n) for n in input().split()]
    instruction = input()

    visited_R = [[] for _ in range(R+1)] # visited_R[r]: for row r, the interval of squares visited
    visited_C = [[] for _ in range(C+1)]

    visited_R[Sr].append([Sc, Sc])
    visited_C[Sc].append([Sr, Sr])
    curr_r, curr_c = Sr, Sc
    for c in instruction:
        if c == 'E' or c == 'W':
            l, r = 0, len(visited_R[curr_r]) - 1
            while l <= r:
                mid = (l + r) // 2
                # There must exist a interval containing current square
                if visited_R[curr_r][mid][0] <= curr_c and curr_c <= visited_R[curr_r][mid][1]:
                    if c == 'E':
                        curr_c = visited_R[curr_r][mid][1] + 1
                        # Update visited_R for new square
                        insert_interval(visited_R[curr_r], mid + 1, curr_c)
                    elif c == 'W':
                        curr_c = visited_R[curr_r][mid][0] - 1
                        insert_interval(visited_R[curr_r], mid, curr_c)
                    break
                elif visited_R[curr_r][mid][0] < curr_c:
                    l = mid + 1
                else:
                    r = mid - 1
            # Update visited_C for new square, there must NOT exist a interval containing new square
            insert_not_exist_new_square(visited_C[curr_c], curr_r)
        elif c == 'N' or c == 'S':
            l, r = 0, len(visited_C[curr_c]) - 1
            while l <= r:
                mid = (l + r) // 2
                if visited_C[curr_c][mid][0] <= curr_r and curr_r <= visited_C[curr_c][mid][1]:
                    if c == 'N':
                        curr_r = visited_C[curr_c][mid][0] - 1
                        insert_interval(visited_C[curr_c], mid, curr_r)
                    elif c == 'S':
                        curr_r = visited_C[curr_c][mid][1] + 1
                        insert_interval(visited_C[curr_c], mid + 1, curr_r)
                    break
                elif visited_C[curr_c][mid][0] < curr_r:
                    l = mid + 1
                else:
                    r = mid - 1
            insert_not_exist_new_square(visited_R[curr_r], curr_c)
        # print(c, curr_r, curr_c)
        # print(visited_R[curr_r])
        # print(visited_C[curr_c])
    print(f"Case #{t + 1}: {curr_r} {curr_c}")
