# Hamiltonian Tour
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000008caa74/0000000000acf318
# Only pass test set 1

T = int(input())
for t in range(T):
    [R, C] = [int(x) for x in input().split()]
    grid = []
    for _ in range(R):
        temp = input()
        row = []
        for c in temp:
            row.append(c)
            row.append(c)
        grid.append(row.copy())
        grid.append(row.copy())

    empty_cell = 0
    R *= 2
    C *= 2
    for i in range(R):
        for j in range(C):
            if grid[i][j] == '*':
                empty_cell += 1
    #     print(grid[i])
    # print(empty_cell)

    ans = ""
    step_count = 0
    now_r = 0
    now_c = 0
    direction = 'E'
    while True:
        step_count += 1
        # print(now_r, now_c, direction)
        if direction == 'E':
            now_c += 1
        elif direction == 'S':
            now_r += 1
        elif direction == 'W':
            now_c -= 1
        elif direction == 'N':
            now_r -= 1
        grid[now_r][now_c] = direction
        ans += direction

        if now_r == 0 and now_c == 0:
            break

        if now_r % 2 == 0 and now_c % 2 == 0:
            if now_r != 0 and grid[now_r-1][now_c] == '*':
                direction = 'N'
            elif now_c != C - 1 and grid[now_r][now_c+1] == '*':
                direction = 'E'
            else:
                break
        elif now_r % 2 == 0 and now_c % 2 == 1:
            if now_c != C - 1 and grid[now_r][now_c+1] == '*':
                direction = 'E'
            elif now_r != R - 1 and grid[now_r+1][now_c] == '*':
                direction = 'S'
            else:
                break
        elif now_r % 2 == 1 and now_c % 2 == 0:
            if now_r != 0 and grid[now_r-1][now_c] == '*':
                direction = 'N'
            elif now_c != 0 and grid[now_r][now_c-1] == '*':
                direction = 'W'
            else:
                break
        elif now_r % 2 == 1 and now_c % 2 == 1:
            if now_r != R - 1 and grid[now_r+1][now_c] == '*':
                direction = 'S'
            elif now_c != 0 and grid[now_r][now_c-1] == '*':
                direction = 'W'
            else:
                break

    # for i in range(R):
    #     print(grid[i])

    if step_count != empty_cell:
        print(f"Case #{t + 1}: IMPOSSIBLE")
    else:
        print(f"Case #{t + 1}: {ans}")
