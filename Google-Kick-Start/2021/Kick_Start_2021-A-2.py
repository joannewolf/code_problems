# L Shaped Plots
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000436140/000000000068c509
# O(R*C)

T = input()
for t in range(int(T)):
    [R, C] = [int(n) for n in input().split()]
    grid = []
    for i in range(R):
        grid.append([int(n) for n in input().split()])
    # print(grid)

    # grid_left[i][j]: starting from grid[i][j], what's the longest segment on its left side (inclusive)
    grid_left = [[0] * C for i in range(R)]
    grid_right = [[0] * C for i in range(R)]
    grid_up = [[0] * C for i in range(R)]
    grid_down = [[0] * C for i in range(R)]
    for i in range(R):
        grid_left[i][0] = grid[i][0]
        grid_right[i][C - 1] = grid[i][C - 1]
    for j in range(C):
        grid_up[0][j] = grid[0][j]
        grid_down[R - 1][j] = grid[R - 1][j]
    for i in range(1, R):
        for j in range(C):
            if (grid[i][j] == 1):
                grid_up[i][j] = grid_up[i - 1][j] + 1
            if (grid[R - 1 - i][j] == 1):
                grid_down[R - 1 - i][j] = grid_down[R - i][j] + 1
    for j in range(1, C):
        for i in range(R):
            if (grid[i][j] == 1):
                grid_left[i][j] = grid_left[i][j - 1] + 1
            if (grid[i][C - 1 - j] == 1):
                grid_right[i][C - 1 - j] = grid_right[i][C - j] + 1
    # print(grid_left)
    # print(grid_right)
    # print(grid_up)
    # print(grid_down)

    # Check each cell, calculate if it's intersection, how many L-shape can it form
    result = 0
    for i in range(R):
        for j in range(C):
            # print("grid {} {} is {}! {} {} {} {}".format(i, j, grid[i][j], grid_left[i][j], grid_right[i][j], grid_up[i][j], grid_down[i][j]))
            # If take up edge as shorter edge, is there valid left/right longer edge?
            result += max(min(grid_up[i][j], grid_right[i][j] // 2) - 1, 0)
            result += max(min(grid_up[i][j], grid_left[i][j] // 2) - 1, 0)
            result += max(min(grid_down[i][j], grid_right[i][j] // 2) - 1, 0)
            result += max(min(grid_down[i][j], grid_left[i][j] // 2) - 1, 0)
            result += max(min(grid_left[i][j], grid_up[i][j] // 2) - 1, 0)
            result += max(min(grid_left[i][j], grid_down[i][j] // 2) - 1, 0)
            result += max(min(grid_right[i][j], grid_up[i][j] // 2) - 1, 0)
            result += max(min(grid_right[i][j], grid_down[i][j] // 2) - 1, 0)
            # print(result)

    print("Case #{}: {}".format(t + 1, result))
