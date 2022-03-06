# Diagonal Puzzle
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050edd/00000000001a2835
# O(N^2)
# Choose two main diagonal and determine they are flipped / not flipped initially, so there are 4 initial settings
# Then all other diagonals can be decided deterministically, choose the legal cases and with minimum flip count
# When N = 6 (even number)
# When main \ (A) is decided, we can determine whether to flip / which intersect with main \
# Then we can determine to flip other \ which intersect with above /
# Eventually we can set up A's and a's; similar for B's and b's, and we can cover all cells
# A.a.a.    .b.b.B
# .A.a.a    b.b.B.
# a.A.a.    .b.B.b
# .a.A.a    b.B.b.
# a.a.A.    .B.b.b
# .a.a.A    B.b.b.
# When N = 7 (odd number), the B is the second largest / diagonal
# If we choose the largest /, it will duplicate with A, but we want it to cover the other set of cells
# A.a.a.a   .b.b.b.
# .A.a.a.   b.b.b.B
# a.A.a.a   .b.b.B.
# .a.A.a.   b.b.B.b
# a.a.A.a   .b.B.b.
# .a.a.A.   b.B.b.b
# a.a.a.A   .B.b.b.

import copy

def print_board(grid):
    for i in range(N):
        print([int(b) for b in grid[i]])
    print()

def check_board(grid):
    flip_count = 0
    print_board(grid)

    flip_needed = [False] * N
    # Check main \ diagonal
    for i in range(N):
        # Flip / diagonal intersecting with main \
        main_r, main_c = i, i
        main_flip = False
        if not grid[main_r][main_c]:
            flip_count += 1
            main_flip = True
            grid[main_r][main_c] = not grid[main_r][main_c]
        # Check upper right direction
        r, c = main_r - 1, main_c + 1
        flag = 1
        while r >= 0 and c < N:
            if main_flip:
                grid[r][c] = not grid[r][c]
            if not grid[r][c]:
                flip_needed[flag] = True
            flag += 1
            c += 1
            r -= 1
        # Check lower left direction
        r, c = main_r + 1, main_c - 1
        flag = -1
        while r < N and c >= 0:
            if main_flip:
                grid[r][c] = not grid[r][c]
            if not grid[r][c]:
                flip_needed[flag] = True
            flag -= 1
            c -= 1
            r += 1
    # Check other \ diagonals which intersect with above / diagonals
    for i in range(1, (N + 1) // 2):
        if flip_needed[i]:
            flip_count += 1
            r, c = 0, 2 * i
            while c < N:
                grid[r][c] = not grid[r][c]
                c += 1
                r += 1
    for i in range(-1, -(N + 1) // 2, -1):
        if flip_needed[i]:
            flip_count += 1
            r, c = 2 * (-i), 0
            while r < N:
                grid[r][c] = not grid[r][c]
                c += 1
                r += 1
    print_board(grid)

    flip_needed = [False] * N
    # Check main / diagonal
    for i in range(flag_odd, N):
        # Flip \ diagonal intersecting with main /
        main_r, main_c = i, N - 1 + flag_odd - i
        main_flip = False
        if not grid[main_r][main_c]:
            flip_count += 1
            main_flip = True
            grid[main_r][main_c] = not grid[main_r][main_c]
        # Check upper left direction
        r, c = main_r - 1, main_c - 1
        flag = -1
        while r >= 0 and c >= 0:
            if main_flip:
                grid[r][c] = not grid[r][c]
            if not grid[r][c]:
                flip_needed[flag] = True
            flag -= 1
            c -= 1
            r -= 1
        # Check lower right direction
        r, c = main_r + 1, main_c + 1
        flag = 1
        while r < N and c < N:
            if main_flip:
                grid[r][c] = not grid[r][c]
            if not grid[r][c]:
                flip_needed[flag] = True
            flag += 1
            c += 1
            r += 1
    # Check other / diagonals which intersect with above \ diagonals
    for i in range(1, N // 2):
        if flip_needed[i]:
            flip_count += 1
            r, c = 2 * i + flag_odd, N - 1
            while r < N:
                grid[r][c] = not grid[r][c]
                c -= 1
                r += 1
    for i in range(-1, -(N + 1) // 2, -1):
        if flip_needed[i]:
            flip_count += 1
            r, c = 0, N - 1 + flag_odd + 2 * i
            while c >= 0:
                grid[r][c] = not grid[r][c]
                c -= 1
                r += 1
    print_board(grid)
    print(flip_count)

    # Check if whole board become black
    for i in range(N):
        for j in range(N):
            if not grid[i][j]:
                return -1
    return flip_count

INT_MAX = 1000
T = int(input())
for t in range(T):
    N = int(input())
    grid = []
    for _ in range(N):
        row = [c == '#' for c in input()] # True is black, False is white
        grid.append(row)

    flag_odd = N % 2
    ans = INT_MAX
    # Both not flip
    grid1 = copy.deepcopy(grid)
    option1 = check_board(grid1)
    if option1 != -1:
        ans = min(ans, option1)

    # Flip only main \ diagonal
    grid2 = copy.deepcopy(grid)
    for i in range(N):
        grid2[i][i] = not grid2[i][i]
    option2 = check_board(grid2)
    if option2 != -1:
        ans = min(ans, option2 + 1)

    # Flip only main / diagonal
    grid3 = copy.deepcopy(grid)
    for i in range(flag_odd, N):
        grid3[i][N - 1 + flag_odd - i] = not grid3[i][N - 1 + flag_odd - i]
    option3 = check_board(grid3)
    if option3 != -1:
        ans = min(ans, option3 + 1)

    # Flip both main / and main \ diagonal
    grid4 = copy.deepcopy(grid)
    for i in range(N):
        grid4[i][i] = not grid4[i][i]
    for i in range(flag_odd, N):
        grid4[i][N - 1 + flag_odd - i] = not grid4[i][N - 1 + flag_odd - i]
    option4 = check_board(grid4)
    if option4 != -1:
        ans = min(ans, option4 + 2)

    # print(option1, option2, option3, option4)
    print(f"Case #{t + 1}: {ans}")
