# Hamiltonian Tour
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000008caa74/0000000000acf318
# Create counterwise circle steps for each empty cell, then use BFS to merge empty cells

T = int(input())
for t in range(T):
    [R, C] = [int(x) for x in input().split()]
    map = []
    grid = []
    empty_cell = 0
    for _ in range(R):
        temp = input()
        map.append(temp)
        row1 = []
        row2 = []
        for c in temp:
            if c == '*':
                row1 += ["E", "S"]
                row2 += ["N", "W"]
                empty_cell += 1
            else:
                row1 += ["#", "#"]
                row2 += ["#", "#"]
        grid.append(row1)
        grid.append(row2)

    # Use BFS to traverse all empty cells
    checked = set()
    queue = []
    for i in range(R):
        for j in range(C):
            if map[i][j] == '*':
                queue.append((i, j))
                break
        if queue:
            break
    # print(queue)
    while queue:
        (now_r, now_c) = queue.pop(0)
        if (now_r, now_c) in checked:
            continue
        checked.add((now_r, now_c))

        # Merge current cell to some checked neighbor cell
        if now_r != 0 and (now_r - 1, now_c) in checked:
            grid[now_r * 2 - 1][now_c * 2 + 1] = 'S'
            grid[now_r * 2][now_c * 2] = 'N'
        elif now_r != R - 1 and (now_r + 1, now_c) in checked:
            grid[now_r * 2 + 1][now_c * 2 + 1] = 'S'
            grid[now_r * 2 + 2][now_c * 2] = 'N'
        elif now_c != 0 and (now_r, now_c - 1) in checked:
            grid[now_r * 2][now_c * 2 - 1] = 'E'
            grid[now_r * 2 + 1][now_c * 2] = 'W'
        elif now_c != C - 1 and (now_r, now_c + 1) in checked:
            grid[now_r * 2][now_c * 2 + 1] = 'E'
            grid[now_r * 2 + 1][now_c * 2 + 2] = 'W'

        # Add unchecked neighbors to queue
        if now_r != 0 and map[now_r - 1][now_c] == '*' and (now_r - 1, now_c) not in checked:
            queue.append((now_r - 1, now_c))
        if now_r != R - 1 and map[now_r + 1][now_c] == '*' and (now_r + 1, now_c) not in checked:
            queue.append((now_r + 1, now_c))
        if now_c != 0 and map[now_r][now_c - 1] == '*' and (now_r, now_c - 1) not in checked:
            queue.append((now_r, now_c - 1))
        if now_c != C - 1 and map[now_r][now_c + 1] == '*' and (now_r, now_c + 1) not in checked:
            queue.append((now_r, now_c + 1))

    # for i in range(R*2):
    #     print(grid[i])

    if len(checked) != empty_cell:
        print(f"Case #{t + 1}: IMPOSSIBLE")
    else:
        ans = ""
        now_r = 0
        now_c = 0
        while True:
            ans += grid[now_r][now_c]
            if grid[now_r][now_c] == 'E':
                now_c += 1
            elif grid[now_r][now_c] == 'S':
                now_r += 1
            elif grid[now_r][now_c] == 'W':
                now_c -= 1
            elif grid[now_r][now_c] == 'N':
                now_r -= 1
            
            if now_r == 0 and now_c == 0:
                break
        print(f"Case #{t + 1}: {ans}")
