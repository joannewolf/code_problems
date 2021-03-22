# Pylons
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000051635/0000000000104e03
# brute-force DFS find all possible path

import copy

def jump(galaxy, path, current_r, current_c):
    if (len(path) == len(galaxy) * len(galaxy[0])):
        return path
    else:
        # find next jump
        for i in range(R):
            for j in range(C):
                if (galaxy[i][j] == 0 and i != current_r and j != current_c and abs(i - current_r) != abs(j - current_c)):
                    # print("jump [{} {}] -> [{} {}]".format(current_r, current_c, i, j))
                    new_path = path.copy()
                    new_path.append([i, j])
                    new_galaxy = copy.deepcopy(galaxy)
                    new_galaxy[i][j] = len(new_path)
                    # print(new_path)
                    # print(new_galaxy)
                    result_path = jump(new_galaxy, new_path, i, j)
                    if result_path is not None:
                        return result_path
        return None

T = input()
for t in range(int(T)):
    [R, C] = [int(n) for n in input().split()]
    galaxy = [[0] * C for i in range(R)]
    # print(galaxy)

    finish = False
    if (R == C):
        for i in range((R + 1) // 2):
            for j in range(i + 1):
                first_galaxy = copy.deepcopy(galaxy)
                first_galaxy[i][j] = 1
                result_path = jump(first_galaxy, [[i, j]], i, j)
                if result_path is not None:
                    print("Case #{}: POSSIBLE".format(t + 1))
                    for [r, c] in result_path:
                        print("{} {}".format(r + 1, c + 1))
                    finish = True
                    break
            if (finish):
                break
    else:
        for i in range((R + 1) // 2):
            for j in range((C + 1) // 2):
                # print("start from", i, j)
                first_galaxy = copy.deepcopy(galaxy)
                first_galaxy[i][j] = 1
                result_path = jump(first_galaxy, [[i, j]], i, j)
                if result_path is not None:
                    print("Case #{}: POSSIBLE".format(t + 1))
                    for [r, c] in result_path:
                        print("{} {}".format(r + 1, c + 1))
                    finish = True
                    break
            if (finish):
                break

    if (not finish):
        print("Case #{}: IMPOSSIBLE".format(t + 1))
