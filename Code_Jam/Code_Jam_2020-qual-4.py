# https://codingcompetitions.withgoogle.com/codejam/round/000000000019fd27/0000000000209a9e

import sys

# is the char_list's head and tail start diff at index flag
# 101 vs. 101 is not diff, 101 vs. 010 is not diff either; 101 vs. 100 is diff
def isStartDiff(char_list, flag):
    assert flag > 0
    same = [char_list[i] == char_list[len(char_list) - 1 - i] for i in xrange(flag)]
    return not (len(set(same)) == 1)

# adjust ans char list when random action happens
def adjust_char_list(char_list, check_two_bits, index):
    assert char_list[index] != 'x' and char_list[index + 1] != 'x' and char_list[-1 - index] != 'x' and char_list[-2 - index] != 'x'
    # array no change
    if char_list[index: index + 2] == check_two_bits:
        return char_list
    # array reversed
    elif list(reversed(char_list))[index: index + 2] == check_two_bits:
        return list(reversed(char_list))
    # array complemented
    elif ['0' if x == '1' else '1' for x in char_list[index: index + 2]] == check_two_bits:
        return ['0' if x == '1' else '1' if x == '0' else 'x' for x in char_list]
    # array reversed and complemented
    elif ['0' if x == '1' else '1' for x in list(reversed(char_list))[index: index + 2]] == check_two_bits:
        return ['0' if x == '1' else '1' if x == '0' else 'x' for x in list(reversed(char_list))]

[T, B] = [int(i) for i in raw_input().split(' ')]
for t in xrange(T):
    ans = ['x'] * B
    start_diff = -1 # start from 1
    asked_time = 0
    while 'x' in ans:
        # if asked_time is some 10-th, check and adjust ans bits
        if asked_time > 0 and asked_time % 10 == 0:
            check_two_bits = []
            if start_diff < 0:
                print 1
                sys.stdout.flush()
                check_two_bits.append(raw_input())
                print 2
                sys.stdout.flush()
                check_two_bits.append(raw_input())
                ans = adjust_char_list(ans, check_two_bits, 0)
            else:
                print start_diff - 1
                sys.stdout.flush()
                check_two_bits.append(raw_input())
                print start_diff
                sys.stdout.flush()
                check_two_bits.append(raw_input())
                ans = adjust_char_list(ans, check_two_bits, start_diff - 2)
            asked_time += 2

        if start_diff < 0 and abs(start_diff) <= B / 2:
            # find where the head and the tail start to be different
            # if start_diff < 0, means not yet reach the diff bit; once found diff bit, flip start_diff to positive
            print 0 + abs(start_diff)
            sys.stdout.flush()
            ans[abs(start_diff) - 1] = raw_input()

            print B + 1 - abs(start_diff)
            sys.stdout.flush()
            ans[B - abs(start_diff)] = raw_input()

            asked_time += 2
            if isStartDiff(ans, abs(start_diff)):
                start_diff = -start_diff
            else:
                start_diff -= 1
        # find next unseen bit
        elif start_diff > 0:
            next = ans.index('x')
            print next + 1
            sys.stdout.flush()
            ans[next] = raw_input()
            asked_time += 1

    print "".join(ans)
    sys.stdout.flush()
    response = raw_input()
    if response == "N":
        sys.exit(1)
