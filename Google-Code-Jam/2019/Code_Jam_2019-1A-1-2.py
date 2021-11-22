# Pylons
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000051635/0000000000104e03
# DFS + random

import copy
from random import randint

def random_jump(galaxy, path):
    if (len(path) == len(galaxy) * len(galaxy[0])):
        return path
    else:
        current_r = path[-1][0]
        current_c = path[-1][1]
        # find next jump randomly
        valid_moves = []
        for i in range(R):
            for j in range(C):
                if (galaxy[i][j] == 0 and i != current_r and j != current_c and abs(i - current_r) != abs(j - current_c)):
                    valid_moves.append([i, j])
        # print(valid_moves)
        if not valid_moves:
            return None
        else:
            next_move = randint(0, len(valid_moves) - 1)
            new_path = path.copy()
            new_path.append(valid_moves[next_move])
            new_galaxy = copy.deepcopy(galaxy)
            new_galaxy[valid_moves[next_move][0]][valid_moves[next_move][1]] = len(new_path)
            # print("jump [{} {}] -> [{} {}]".format(current_r, current_c, valid_moves[next_move][0], valid_moves[next_move][1]))
            # print(new_path)
            # print(new_galaxy)
            return random_jump(new_galaxy, new_path)

T = input()
for t in range(int(T)):
    [R, C] = [int(n) for n in input().split()]

    if ((min(R, C) == 2 and max(R, C) in [2, 3, 4]) or (R == 3 and C == 3)):
        print("Case #{}: IMPOSSIBLE".format(t + 1))
        continue

    galaxy = [[0] * C for i in range(R)]
    # print(galaxy)

    while True:
        i = randint(0, R - 1)
        j = randint(0, C - 1)
        first_galaxy = copy.deepcopy(galaxy)
        first_galaxy[i][j] = 1
        # print("start from", i, j)
        result_path = random_jump(first_galaxy, [[i, j]])
        if result_path is not None:
            print("Case #{}: POSSIBLE".format(t + 1))
            for [r, c] in result_path:
                print("{} {}".format(r + 1, c + 1))
            break
