# Moons and Umbrellas
# https://codingcompetitions.withgoogle.com/codejam/round/000000000043580a/00000000006d1145
# Including test set 3, using dp

T = input()
for t in range(int(T)):
    [X, Y, S] = input().split()
    X = int(X)
    Y = int(Y)
    # dp_c[i] means if S[i] == 'C', the min value of S[i:]
    # if S[i] == '?', both dp_c[i] and dp_j[i] will have value; if S[i] == 'C' or 'J', only dp_c[i] or dp_j[i] will have value
    dp_c = [0] * len(S)
    dp_j = [0] * len(S)
    for i in range(len(S) - 2, -1, -1):
        if (S[i] == '?' and S[i + 1] == '?'):
            dp_c[i] = min(dp_c[i + 1], X + dp_j[i + 1]) # 'CC...' or 'CJ...'
            dp_j[i] = min(dp_j[i + 1], Y + dp_c[i + 1]) # 'JJ...' or 'JC...'
        elif (S[i] == '?' and S[i + 1] == 'C'):
            dp_c[i] = dp_c[i + 1]
            dp_j[i] = Y + dp_c[i + 1]
        elif (S[i] == '?' and S[i + 1] == 'J'):
            dp_c[i] = X + dp_j[i + 1]
            dp_j[i] = dp_j[i + 1]
        elif (S[i] == 'C' and S[i + 1] == '?'):
            dp_c[i] = min(dp_c[i + 1], X + dp_j[i + 1])
        elif (S[i] == 'C' and S[i + 1] == 'C'):
            dp_c[i] = dp_c[i + 1]
        elif (S[i] == 'C' and S[i + 1] == 'J'):
            dp_c[i] = X + dp_j[i + 1]
        elif (S[i] == 'J' and S[i + 1] == '?'):
            dp_j[i] = min(dp_j[i + 1], Y + dp_c[i + 1])
        elif (S[i] == 'J' and S[i + 1] == 'C'):
            dp_j[i] = Y + dp_c[i + 1]
        elif (S[i] == 'J' and S[i + 1] == 'J'):
            dp_j[i] = dp_j[i + 1]

    if S[0] == '?':
        result = min(dp_c[0], dp_j[0])
    elif S[0] == 'C':
        result = dp_c[0]
    elif S[0] == 'J':
        result = dp_j[0]

    print("Case #{}: {}".format(t + 1, result))
