# Funniest Word Search
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050ee1/00000000000510f0
# Brute-force, let V = sum{word length} <= 5000, O(RCV + 3R^2C + 3RC^2 + R^2C^2), TLE but correct locally on test set 1

ascii_A = ord('A')

def gcd(a, b):
    while (a % b) > 0:
        a, b = b, a % b
    return b

T = int(input())
for t in range(T):
    [R, C, W] = [int(x) for x in input().split()]
    grid = []
    for _ in range(R):
        grid.append(input())
    words = [[] for _ in range(26)]
    for _ in range(W):
        word = input()
        words[ord(word[0]) - ascii_A].append(word)

    match_h = [[[0] * (C+1) for _ in range(C)] for _ in range(R)]
    # match_h[r][c][l]: Starting from grid[r][c], the sum{len} of horizontal matching words with length l to the right
    match_v = [[[0] * (R+1) for _ in range(C)] for _ in range(R)]
    # match_v[r][c][l]: Starting from grid[r][c], the sum{len} of vertical matching words with length l to the below

    # Count matching words
    for r in range(R):
        for c in range(C):
            for w in words[ord(grid[r][c]) - ascii_A]:
                n = len(w)
                # From left to right
                match = True
                for i in range(n):
                    if c + i >= C or grid[r][c + i] != w[i]:
                        match = False
                        break
                if match:
                    match_h[r][c][n] += n
                # From right to left
                match = True
                for i in range(n):
                    if c + i < 0 or grid[r][c - i] != w[i]:
                        match = False
                        break
                if match:
                    match_h[r][c - n + 1][n] += n
                # From up to down
                match = True
                for i in range(n):
                    if r + i >= R or grid[r + i][c] != w[i]:
                        match = False
                        break
                if match:
                    match_v[r][c][n] += n
                # From down to up
                match = True
                for i in range(n):
                    if r - i < 0 or grid[r - i][c] != w[i]:
                        match = False
                        break
                if match:
                    match_v[r - n + 1][c][n] += n

    # print("match_v")
    # for r in range(R):
    #     for c in range(C):
    #         print("r", r, "c", c, match_v[r][c])
    # print("match_h")
    # for r in range(R):
    #     for c in range(C):
    #         print("r", r, "c", c, match_h[r][c])

    # new match_h[r][c][l]: Starting from grid[r][c], the sum{len} of horizontal matching words <= length l to the right
    # new match_v[r][c][l]: Starting from grid[r][c], the sum{len} of vertical matching words <= length l to the below
    for r in range(R):
        for c in range(C):
            for i in range(1, C+1):
                match_h[r][c][i] += match_h[r][c][i-1]
            for i in range(1, R+1):
                match_v[r][c][i] += match_v[r][c][i-1]

    count_v = [[[0] * (C) for _ in range(R)] for _ in range(R)]
    # count_v[r1][r2][c]: Between row r1~r2, the sum{len} of matching words in coloum c
    count_h = [[[0] * (R) for _ in range(C)] for _ in range(C)]
    # count_h[c1][c2][r]: Between column c1~c2, the sum{len} of matching words in row r

    for r1 in range(0, R):
        for r2 in range(r1, R):
            n = r2 - r1 + 1
            for c in range(C):
                # Count # of vertical words between row r1~r2
                count = 0
                for i in range(n):
                    count += match_v[r1 + i][c][n - i]
                count_v[r1][r2][c] = count
    for c1 in range(0, C):
        for c2 in range(c1, C):
            n = c2 - c1 + 1
            for r in range(R):
                # Count # of horizontal words between column c1~c2
                count = 0
                for i in range(n):
                    count += match_h[r][c1 + i][n - i]
                count_h[c1][c2][r] = count

    # new count_v[r1][r2][c]: Between row r1~r2, the sum{len} of matching words from column 1~c
    for r1 in range(0, R):
        for r2 in range(r1, R):
            for c in range(1, C):
                count_v[r1][r2][c] += count_v[r1][r2][c-1]
    # new count_h[c1][c2][r]: Between column c1~c2, the sum{len} of matching words from row 1~r
    for c1 in range(0, C):
        for c2 in range(c1, C):
            for r in range(1, R):
                count_h[c1][c2][r] += count_h[c1][c2][r-1]

    max_fun = (-1, 1)
    fun_count = 0
    for r1 in range(0, R):
        for r2 in range(r1, R):
            for c1 in range(0, C):
                for c2 in range(c1, C):
                    len_r = r2 - r1 + 1
                    len_c = c2 - c1 + 1
                    sum = count_v[r1][r2][c2] + count_h[c1][c2][r2]
                    if c1 != 0:
                        sum -= count_v[r1][r2][c1-1]
                    if r1 != 0:
                        sum -= count_h[c1][c2][r1-1]
                    if sum / (len_r + len_c) > max_fun[0] / max_fun[1]:
                        max_fun = (sum, len_r + len_c)
                        fun_count = 1
                    elif sum / (len_r + len_c) == max_fun[0] / max_fun[1]:
                        fun_count += 1

    g = gcd(max_fun[0], max_fun[1])
    print(f"Case #{t + 1}: {max_fun[0]//g}/{max_fun[1]//g} {fun_count}")
