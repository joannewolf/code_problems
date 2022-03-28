# Inversions Organize
# https://codingcompetitions.withgoogle.com/codejamio/round/00000000009d9870/0000000000a33e95

T = int(input())
for t in range(T):
    N = int(input())
    grid = []
    for _ in range(2 * N):
        grid.append(input())

    upper_left = 0
    upper_right = 0
    lower_left = 0
    lower_right = 0
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 'I':
                upper_left += 1
        for j in range(N, 2 * N):
            if grid[i][j] == 'I':
                upper_right += 1
    for i in range(N, 2 * N):
        for j in range(N):
            if grid[i][j] == 'I':
                lower_left += 1
        for j in range(N, 2 * N):
            if grid[i][j] == 'I':
                lower_right += 1
    ans = abs(upper_left - lower_right) + abs(upper_right - lower_left)
    print(f"Case #{t + 1}: {ans}")
