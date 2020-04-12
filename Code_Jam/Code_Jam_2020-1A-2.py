# https://codingcompetitions.withgoogle.com/codejam/round/000000000019fd74/00000000002b1353
# the sum of r-th row = 2^(r - 1), follow N's binary bit to decide which row to go through
# since N <= 10^9 < 2^30, we will use less than 30 rows
# however, since the sequence has to be continuous, we might take some additional 1's
# we can instead construct N - 30 and then add 1's to adjust to N

T = int(raw_input())
for t in xrange(T):
    N = int(raw_input())
    print "Case #{}:".format(t + 1)

    if N - 30 <= 0:
        for i in xrange(1, N + 1):
            print "{} {}".format(i, 1)
    else:
        new_N = N - 30
        zero_bits_count = 0
        row = 1
        current_side = 'L'
        while new_N != 0:
            # when bit == 1, go through r-th row to the other side
            if new_N % 2 == 1:
                if current_side == 'L':
                    for i in xrange(1, row + 1):
                        print "{} {}".format(row, i)
                    current_side = 'R'
                else:
                    for i in xrange(row, 0, -1):
                        print "{} {}".format(row, i)
                    current_side = 'L'
            # when bit == 0, go to next 1 on the same side
            else:
                zero_bits_count += 1
                if current_side == 'L':
                    print "{} {}".format(row, 1)
                else:
                    print "{} {}".format(row, row)
            new_N >>= 1
            row += 1
        # add remaining 1's
        if current_side == 'L':
            for i in xrange(30 - zero_bits_count):
                print "{} {}".format(row + i, 1)
        else:
            for i in xrange(30 - zero_bits_count):
                print "{} {}".format(row + i, row + i)