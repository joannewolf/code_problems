# Rabbit House
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000436140/000000000068cb14
# Starting from H = max(grid[i][j]), if its neighbor has height difference greater than 1, make it as H - 1
# Then continue with the second max height grid and so on until all grid are checked
# O(different height value * R*C) = O((R*C) * R*C), pass test set 1

T = input()
for t in range(int(T)):
    [R, C] = [int(n) for n in input().split()]
    grid = []
    for i in range(R):
        grid.append([int(n) for n in input().split()])
    # print(grid)

    result = 0
    max_height = -1
    for i in range(R):
        for j in range(C):
            if (grid[i][j] > max_height):
                max_height = grid[i][j]

    checked = 0
    for h in range(max_height, 0, -1):
        for i in range(R):
            for j in range(C):
                if (grid[i][j] == h):
                    # If the neighbor has height difference > 1, make it h - 1
                    if (i != 0 and abs(grid[i][j] - grid[i - 1][j]) > 1):
                        result += abs((h - 1) - grid[i - 1][j])
                        grid[i - 1][j] = h - 1
                    if (i != R - 1 and abs(grid[i][j] - grid[i + 1][j]) > 1):
                        result += abs((h - 1) - grid[i + 1][j])
                        grid[i + 1][j] = h - 1
                    if (j != 0 and abs(grid[i][j] - grid[i][j - 1]) > 1):
                        result += abs((h - 1) - grid[i][j - 1])
                        grid[i][j - 1] = h - 1
                    if (j != C - 1 and abs(grid[i][j] - grid[i][j + 1]) > 1):
                        result += abs((h - 1) - grid[i][j + 1])
                        grid[i][j + 1] = h - 1
                    checked += 1
        if (checked == R * C):
            break
    # print(grid)

    print("Case #{}: {}".format(t + 1, result))
