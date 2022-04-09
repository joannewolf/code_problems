# Weightlifting
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000877ba5/0000000000aa9280
# Key idea: If there is a multiset which is common to all exercises, it's optimal to put them in the bottom of stacks
# If there's more than 1 exercise, there's at least one time that the stack only contains common weight multiset
# Then divide from that middle point, we can do the divide and conquer by dp
# O(E^2*W + E^3) = O(E^3)

MAX_INT = pow(10, 9)

T = int(input())
for t in range(T):
    [E, W] = [int(x) for x in input().split()]
    exercises = []
    for _ in range(E):
        exercises.append([int(x) for x in input().split()])

    common = [[[] for _ in range(E)] for _ in range(E)]
    # common[l][r]: the common weights that is common to exercises l~r, inclusive, l <= r
    move = [[0] * E for _ in range(E)]
    # move[l][r]: the minimum move to finish exercise l~r, inclusive

    for l in range(E):
        temp_common = exercises[l].copy()
        common[l][l] = temp_common.copy()
        for r in range(l+1, E):
            for i in range(W):
                temp_common[i] = min(temp_common[i], exercises[r][i])
            common[l][r] = temp_common.copy()
    for l in range(E):
        for r in range(E):
            # print("l", l, "r", r, common[l][r], sum(common[l][r]))
            common[l][r] = sum(common[l][r])
    
    for gap in range(1, E):
        for l in range(E - gap):
            r = l + gap
            min_move = MAX_INT
            for x in range(l, r):
                curr_move = move[l][x] + move[x+1][r] + 2 * (common[l][x] - common[l][r]) + 2 * (common[x+1][r] - common[l][r])
                min_move = min(min_move, curr_move)
            move[l][r] = min_move

    print(f"Case #{t + 1}: {move[0][E-1] + 2 * common[0][E-1]}")
