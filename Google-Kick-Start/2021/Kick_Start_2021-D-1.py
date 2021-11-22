# Arithmetic Square
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000004361e3/000000000082b813

T = int(input())
for t in range(T):
    grid = []
    grid.append([int(n) for n in input().split()])
    grid.append([int(n) for n in input().split()])
    grid[1].insert(1, -1)
    grid.append([int(n) for n in input().split()])
    # print(grid)

    result = 0
    # For seq crossing middle grid
    dict = {}
    keys = []
    keys.append((grid[1][0] + grid[1][2]) / 2)
    keys.append((grid[0][1] + grid[2][1]) / 2)
    keys.append((grid[0][0] + grid[2][2]) / 2)
    keys.append((grid[0][2] + grid[2][0]) / 2)
    for key in keys:
        if key.is_integer():
            if key in dict:
                dict[key] += 1
            else:
                dict[key] = 1
    if dict:
        result += max(dict.values())

    # For seq not crossing middle grid
    if grid[0][1] == (grid[0][0] + grid[0][2]) / 2:
        result += 1
    if grid[2][1] == (grid[2][0] + grid[2][2]) / 2:
        result += 1
    if grid[1][0] == (grid[0][0] + grid[2][0]) / 2:
        result += 1
    if grid[1][2] == (grid[0][2] + grid[2][2]) / 2:
        result += 1

    print(f"Case #{t + 1}: {result}")
