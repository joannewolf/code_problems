# https://codingcompetitions.withgoogle.com/codejam/round/000000000019fef4/0000000000317409

T = int(raw_input())
for t in xrange(T):
    X, Y, M = [n for n in raw_input().split(' ')]
    X = int(X)
    Y = int(Y)

    done = -1
    for i in range(len(M) + 1):
        if abs(X) + abs(Y) <= i:
            print "Case #{}: {}".format(t + 1, i)
            break
        elif i == len(M):
            print "Case #{}: IMPOSSIBLE".format(t + 1)
        elif M[i] == 'E':
            X += 1
        elif M[i] == 'W':
            X -= 1
        elif M[i] == 'N':
            Y += 1
        elif M[i] == 'S':
            Y -= 1
