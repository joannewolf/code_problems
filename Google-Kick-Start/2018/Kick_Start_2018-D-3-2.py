# Funniest Word Search
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050ee1/00000000000510f0
# Optimized brute-force, O(RCW + R^2C + RC^2 + R^2C^2) = O(R^2C^2), MLE but correct locally on test set 1

ascii_A = ord('A')

def is_palindrome(s: str):
    n = len(s)
    for i in range(n // 2):
        if s[i] != s[n - i - 1]:
            return False
    return True

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
    word_len = set()
    words = {}
    for _ in range(W):
        word = input()
        n = len(word)
        word_len.add(n)
        if n not in words:
            words[n] = {}
            words[n][word] = 1
        elif word not in words[n]:
            words[n][word] = 1
        else:
            words[n][word] += 1

        word_reversed = word[::-1]
        if word_reversed not in words[n]:
            words[n][word_reversed] = 1
        else:
            words[n][word_reversed] += 1
    word_len = sorted(list(word_len))
    # print(word_len)
    # print(words)

    match_h = [[[0] * (C+1) for _ in range(C)] for _ in range(R)]
    # match_h[r][c][l]: Starting from grid[r][c], the sum{len} of horizontal matching words with length l to the right
    match_v = [[[0] * (R+1) for _ in range(C)] for _ in range(R)]
    # match_v[r][c][l]: Starting from grid[r][c], the sum{len} of vertical matching words with length l to the below

    # Count matching words
    for r in range(R):
        for c in range(C):
            for l in word_len:
                # Check horizontal substr
                if c + l - 1 < C:
                    substr = grid[r][c : c+l]
                    if substr in words[l]:
                        match_h[r][c][l] += words[l][substr] * l
                # Check vertical substr
                if r + l - 1 < R:
                    substr = ""
                    for i in range(r, r+l):
                        substr += grid[i][c]
                    if substr in words[l]:
                        match_v[r][c][l] += words[l][substr] * l

    # print("match_v")
    # for r in range(R):
    #     for c in range(C):
    #         print("r", r, "c", c, match_v[r][c])
    # print("match_h")
    # for r in range(R):
    #     for c in range(C):
    #         print("r", r, "c", c, match_h[r][c])
    # print()

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

    total = [[[[0] * C for _ in range(C)] for _ in range(R)] for _ in range(R)]
    for r1 in range(0, R):
        count_h = [[0] * (C+1) for _ in range(C)]
        # count_h[c][l]: the sum{len} of matching words starting between [r1, c] ~ [r2, c], with length <= l to the right
        for r2 in range(r1, R):
            for c in range(C):
                for l in range(1, C - c + 1):
                    count_h[c][l] += match_h[r2][c][l]
                # print("r1", r1, "r2", r2, "c", c, count_h[c])
            for c2 in range(C - 1, -1, -1):
                total[r1][r2][c2][c2] += count_h[c2][1]
                prev_c = count_h[c2][1]
                # print("c2", c2, count_h[c2][1])
                for c1 in range(c2 - 1, -1, -1):
                    total[r1][r2][c1][c2] += prev_c + count_h[c1][c2 - c1 + 1]
                    prev_c += count_h[c1][c2 - c1 + 1]
                    # print("c2", c2, "c1", c1, total[r1][r2][c1+1][c2], count_h[c1][c2 - c1 + 1], "=", total[r1][r2][c1][c2])
    # print()
    for c1 in range(0, C):
        count_v = [[0] * (R+1) for _ in range(R)]
        # count_v[r][l]: the sum{len} of matching words starting between [r, c1] ~ [r, c2], with length <= l to the down
        for c2 in range(c1, C):
            for r in range(R):
                for l in range(1, R - r + 1):
                    count_v[r][l] += match_v[r][c2][l]
                # print("c1", c1, "c2", c2, "r", r, count_v[r])
            for r2 in range(R - 1, -1, -1):
                total[r2][r2][c1][c2] += count_v[r2][1]
                prev_v = count_v[r2][1]
                # print("r2", r2, count_v[r2][1])
                for r1 in range(r2 - 1, -1, -1):
                    total[r1][r2][c1][c2] += prev_v + count_v[r1][r2 - r1 + 1]
                    prev_v += count_v[r1][r2 - r1 + 1]
                    # print("r2", r2, "r1", r1, total[r1+1][r2][c1][c2], count_v[r1][r2 - r1 + 1], "=", total[r1][r2][c1][c2])
    # print()

    max_fun = (-1, 1)
    fun_count = 0
    for r1 in range(0, R):
        for r2 in range(r1, R):
            for c1 in range(0, C):
                for c2 in range(c1, C):
                    # print("r1", r1, "r2", r2, "c1", c1, "c2", c2, total[r1][r2][c1][c2])
                    len_r = r2 - r1 + 1
                    len_c = c2 - c1 + 1
                    if total[r1][r2][c1][c2] / (len_r + len_c) > max_fun[0] / max_fun[1]:
                        max_fun = (total[r1][r2][c1][c2], len_r + len_c)
                        fun_count = 1
                    elif total[r1][r2][c1][c2] / (len_r + len_c) == max_fun[0] / max_fun[1]:
                        fun_count += 1

    g = gcd(max_fun[0], max_fun[1])
    print(f"Case #{t + 1}: {max_fun[0]//g}/{max_fun[1]//g} {fun_count}")
