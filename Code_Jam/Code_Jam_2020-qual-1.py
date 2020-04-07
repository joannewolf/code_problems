# https://codingcompetitions.withgoogle.com/codejam/round/000000000019fd27/000000000020993c

T = raw_input()
for t in xrange(int(T)):
    N = int(raw_input())
    square = []
    for n in xrange(N):
        square.append([int(a) for a in raw_input().split(' ')])

    trace = 0
    row = 0
    column = 0

    for i in xrange(N):
        trace += square[i][i]

        current_row = square[i][:]
        row += (len(current_row) != len(set(current_row)))

        current_col = [temp_row[i] for temp_row in square]
        column += (len(current_col) != len(set(current_col)))

    print "Case #{}: {} {} {}".format(t + 1, trace, row, column)