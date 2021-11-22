# Rabbit House
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000436140/000000000068cb14
# Starting from H = max(grid[i][j]), if its neighbor has height difference greater than 1, make it as H - 1
# Then continue with the second max height grid and so on until all grid are checked
# Instead of using 3-layer for loop, use bucketing to find grids with next height faster
# Each grid can be at most re-added to bucket 4 times because of its 4 neighbors, O(4*R*C) = O(R*C)

T = input()
for t in range(int(T)):
    [R, C] = [int(n) for n in input().split()]
    grid = []
    for i in range(R):
        grid.append([int(n) for n in input().split()])
    # print(grid)

    result = 0
    max_height = max([max(row) for row in grid])
    bucket = [[] for i in range(max_height + 1)]
    grid_checked = [[False] * C for i in range(R)]
    for i in range(R):
        for j in range(C):
            bucket[grid[i][j]].append((i, j))
    # print(bucket)

    checked = 0
    # The lowest possible height is max_height - R - C + 2, imagine the H is on one corner, and the lowest height will be on opposite corner
    for h in range(max_height, max_height - R - C + 2, -1):
        # print(h, bucket[h])
        for (i, j) in bucket[h]:
            if not grid_checked[i][j]:
                # If the neighbor has height difference > 1, make it h - 1
                if (i != 0 and abs(grid[i][j] - grid[i - 1][j]) > 1):
                    result += abs((h - 1) - grid[i - 1][j])
                    grid[i - 1][j] = h - 1
                    bucket[h - 1].append((i - 1, j))
                if (i != R - 1 and abs(grid[i][j] - grid[i + 1][j]) > 1):
                    result += abs((h - 1) - grid[i + 1][j])
                    grid[i + 1][j] = h - 1
                    bucket[h - 1].append((i + 1, j))
                if (j != 0 and abs(grid[i][j] - grid[i][j - 1]) > 1):
                    result += abs((h - 1) - grid[i][j - 1])
                    grid[i][j - 1] = h - 1
                    bucket[h - 1].append((i, j - 1))
                if (j != C - 1 and abs(grid[i][j] - grid[i][j + 1]) > 1):
                    result += abs((h - 1) - grid[i][j + 1])
                    grid[i][j + 1] = h - 1
                    bucket[h - 1].append((i, j + 1))
                grid_checked[i][j] = True
                checked += 1
        if (checked == R * C):
            break
    # print(grid)

    print("Case #{}: {}".format(t + 1, result))
