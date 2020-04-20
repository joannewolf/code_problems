# https://codingcompetitions.withgoogle.com/codejam/round/000000000019fef2/00000000002d5b62
# If |X|+|Y| % 2 == 0, it's impossible to reach, because we have 2^0 = 1 to move
# If odd on x-axis, we can either move East or West, and the related goal becomes (X - 1, Y) or (X + 1, Y) and next step we need to move 2
# it can be simplified as goal ((X - 1) / 2, Y / 2) or ((X + 1) / 2, Y / 2) and we need to move 1, now the problem is reset
# Same stratefy when odd on y-axis

T = int(raw_input())
for t in xrange(T):
    X, Y = [int(n) for n in raw_input().split(' ')]
    ans = ""

    while (X + Y) % 2 == 1:
        # last step when |X| + |Y| = 1, directly go to goal, don't go further
        if X == -1 and Y == 0:
            ans += "W"
            X += 1
        elif X == 1 and Y == 0:
            ans += "E"
            X -= 1
        elif X == 0 and Y == 1:
            ans += "N"
            Y -= 1
        elif X == 0 and Y == -1:
            ans += "S"
            Y += 1
        # when odd on x-axis
        elif X % 2 == 1:
            if ((X + 1) / 2 + Y / 2) % 2 == 1:
                ans += "W"
                X = (X + 1) / 2
            elif ((X - 1) / 2 + Y / 2) % 2 == 1:
                ans += "E"
                X = (X - 1) / 2
            Y /= 2
        # when odd on y-axis
        else:
            if (X / 2 + (Y + 1) / 2) % 2 == 1:
                ans += "S"
                Y = (Y + 1) / 2
            elif (X / 2 + (Y - 1) / 2) % 2 == 1:
                ans += "N"
                Y = (Y - 1) / 2
            X /= 2

    if X == 0 and Y == 0:
        print "Case #{}: {}".format(t + 1, ans)
    else:
        print "Case #{}: IMPOSSIBLE".format(t + 1)