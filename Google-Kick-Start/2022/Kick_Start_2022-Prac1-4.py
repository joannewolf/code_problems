# Hex
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000008f4332/0000000000942527

T = int(input())
for t in range(T):
    N = int(input())
    grid = []
    for _ in range(N):
        grid.append(list(input()))

    count_b = 0
    count_r = 0
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 'B':
                count_b += 1
            elif grid[i][j] == 'R':
                count_r += 1
    if abs(count_b - count_r) >= 2:
        ans = "Impossible"
    else:
        connected_b = 0
        connected_r = 0
        # Use DFS to check if blue connected
        for i in range(N):
            if grid[i][0] == 'B':
                stack = [(i, 0)]
                while stack:
                    (r, c) = stack.pop(-1)
                    grid[r][c] = 'b'
                    if c == N - 1:
                        connected_b += 1
                        break
                    else:
                        # Priority: up > upper right > right > lower > lower left > left
                        # Put lower priority cell to stack first cuz we pop from back
                        if c != 0 and grid[r][c - 1] == 'B':
                            stack.append((r, c - 1))
                        if r != N - 1 and c != 0 and grid[r + 1][c - 1] == 'B':
                            stack.append((r + 1, c - 1))
                        if r != N - 1 and grid[r + 1][c] == 'B':
                            stack.append((r + 1, c))
                        if grid[r][c + 1] == 'B':
                            stack.append((r, c + 1))
                        if r != 0 and grid[r - 1][c + 1] == 'B':
                            stack.append((r - 1, c + 1))
                        if r != 0 and grid[r - 1][c] == 'B':
                            stack.append((r - 1, c))
            if grid[0][i] == 'R':
                stack = [(0, i)]
                while stack:
                    (r, c) = stack.pop(-1)
                    grid[r][c] = 'r'
                    if r == N - 1:
                        connected_r += 1
                        break
                    else:
                        # Priority: left > lower left > lower > right > upper right > up
                        if r != 0 and grid[r - 1][c] == 'R':
                            stack.append((r - 1, c))
                        if r != 0 and c != N - 1 and grid[r - 1][c + 1] == 'R':
                            stack.append((r - 1, c + 1))
                        if c != N - 1 and grid[r][c + 1] == 'R':
                            stack.append((r, c + 1))
                        if grid[r + 1][c] == 'R':
                            stack.append((r + 1, c))
                        if c != 0 and grid[r + 1][c - 1] == 'R':
                            stack.append((r + 1, c - 1))
                        if c != 0 and grid[r][c - 1] == 'R':
                            stack.append((r, c - 1))

        # print(connected_b, connected_r, count_b, count_r)
        if connected_b + connected_r >= 2:
            ans = "Impossible"
        elif connected_b == 1:
            if count_r > count_b:
                ans = "Impossible"
            else:
                ans = "Blue wins"
        elif connected_r == 1:
            if count_b > count_r:
                ans = "Impossible"
            else:
                ans = "Red wins"
        else:
            ans = "Nobody wins"
        # for i in range(N):
        #     print(" " * i + " ".join(grid[i]))

    print(f"Case #{t + 1}: {ans}")
