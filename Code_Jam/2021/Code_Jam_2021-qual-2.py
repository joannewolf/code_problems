# Moons and Umbrellas
# https://codingcompetitions.withgoogle.com/codejam/round/000000000043580a/00000000006d1145

T = input()
for t in range(int(T)):
    [X, Y, S] = input().split()
    X = int(X)
    Y = int(Y)

    result = 0
    flag = '-'
    for s in S:
        if (s == '?'):
            continue
        elif (s == 'C'):
            if (flag == 'J'):
                result += Y
            flag = 'C'
        elif (s == 'J'):
            if (flag == 'C'):
                result += X
            flag = 'J'

    print("Case #{}: {}".format(t + 1, result))
