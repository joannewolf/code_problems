# Sheepwalking
# https://codingcompetitions.withgoogle.com/codejamio/round/0000000000050fc5/0000000000054edd

T = raw_input()
for t in xrange(int(T)):
    [x, y] = [int(a) for a in raw_input().split(' ')]
    [x, y] = sorted([abs(x), abs(y)]) # x >= 0, y >= 1, x <= y

    # row 0...i...x, col 0...j...y; only i <= j has value (expected steps)
    ans = [[float(0)] * (y + 1) for _ in xrange(x + 2)]
    # ans[0][1] = 0.5 * 1 + 0.5 * (1 + ans[1][1])
    # ans[1][1] = 0.5 * (1 + ans[0][1]) + 0.5 * (1 + ans[0][1])
    ans[0][1] = 3.0
    ans[1][1] = 4.0

    # if i == 0, ans[0][j] = 0.5 * (1 + ans[0][j - 1]) + 0.5 * (1 + ans[1][j])
    #                      = 0.5 * (1 + ans[0][j - 1]) + 0.5 * (1 + (0.5 * (1 + ans[0][j]) + 0.5 * (1 + ans[1][j - 1])))
    #                      = 3/2 + 1/2 * ans[0][j - 1] + 1/4 * ans[0][j] + 1/4 * ans[1][j - 1]
    #            ans[0][j] = 4/3 * (3/2 + 1/2 * ans[0][j - 1] + 1/4 * ans[1][j - 1])
    #                      = 2 + 2/3 * ans[0][j - 1] + 1/3 * ans[1][j - 1]
    # if i != 0, ans[i][j] = 0.5 * (1 + ans[i - 1][j]) + 0.5 * (1 + ans[i][j - 1])
    for j in xrange(2, y + 1):
        ans[0][j] = 2.0 + 2.0/3.0 * ans[0][j - 1] + 1.0/3.0 * ans[1][j - 1]
        ans[1][j] = 1.0 + 0.5 * ans[0][j] + 0.5 * ans[1][j - 1]
        for i in xrange(2, min(x + 1, j + 1)):
            if i == j:
                ans[i][j] = ans[i - 1][j] + 1.0
            else:
                ans[i][j] = 1.0 + 0.5 * ans[i - 1][j] + 0.5 * ans[i][j - 1]

    print "Case #{}: {}".format(t + 1, ans[x][y])