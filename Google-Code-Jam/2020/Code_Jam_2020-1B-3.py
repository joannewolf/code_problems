# Join the Ranks
# https://codingcompetitions.withgoogle.com/codejam/round/000000000019fef2/00000000002d5b64
# 1, 2, ..., R, 1, 2, ..., R, ..., 1, 2, ..., R (S sets 1~R) -> 1, ..., 1 (S 1's), 2, ..., 2 (S 2's), ..., R, ..., R (S R's)

T = int(raw_input())
for t in xrange(T):
    R, S = [int(n) for n in raw_input().split(' ')]

    # start with (R * S - 1) adjacent cards of different ranks -> (R - 1) adjacent cards of different ranks
    # with each operation, we can decrease # of adjacent cards of different ranks by at most 2
    # minimum # of operation = ceil((R * S - R) / 2)
    print "Case #{}: {}".format(t + 1, (R * S - R + 1) / 2)

    # invariant: for every adjacent cards X, Y, it's either Y = X or Y = (X + 1) % R
    # for each operation, pile_A = X, ..., X, X + 1, ..., X + 1; pile_B = X + 2, ..., X - 1, X
    # after operation, deck = X + 2, ..., X, ..., X, X + 1, ..., X + 1, ...
    # pile_B tail = pile_A head, and pile_A tail = remain head, decrease # of adjacent cards of different ranks by 2
    # if in pile_A, |X block| < R, there must exist a X in the remaining deck
    # if (R * S - R) is even, the last operation will make it target order cuz the last element is R
    # if (R * S - R) is odd, before last operation it's like R, ..., R, 1, ..., 1, ..., R - 1, ..., R - 1, R, pile_A = first X block, pile_B = remaining deck
    deck = range(1, R + 1) * S
    for i in range((R * S - R) / 2):
        # print deck
        X = deck[0]
        flag_A = -1
        flag_B = -1
        for j in range(R * S):
            if deck[j] != X:
                flag_A = j
                break
        # print "flag_A", flag_A
        for j in range(flag_A, R * S):
            if (X != R and deck[j] != X + 1) or (X == R and deck[j] != 1):
                flag_A = j
                break
        # print "flag_A", flag_A
        for j in range(flag_A, R * S):
            if deck[j] == X:
                flag_B = j + 1
                break
        # print "flag_B", flag_B

        print "{} {}".format(flag_A, flag_B - flag_A)
        new_deck = deck[flag_A: flag_B] + deck[0: flag_A] + deck[flag_B:]
        deck = new_deck

    # last operation for odd (R * S - R)
    if (R * S - R) % 2 == 1:
        print "{} {}".format(S - 1, R * S - S + 1)