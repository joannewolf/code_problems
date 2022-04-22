# The 4M Corporation
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000201c98/0000000000201c99

INF = pow(10, 10)

T = int(input())
for t in range(T):
    [MIN, MAX, MEAN, MEDIAN] = [int(x) for x in input().split()]

    if MAX < MIN:
        print(f"Case #{t + 1}: IMPOSSIBLE")
    elif MEAN < MIN or MEAN > MAX:
        print(f"Case #{t + 1}: IMPOSSIBLE")
    elif MEDIAN < MIN or MEDIAN > MAX:
        print(f"Case #{t + 1}: IMPOSSIBLE")
    elif MIN == MAX and MIN == MEDIAN and MIN == MEAN:
        print(f"Case #{t + 1}: 1")
    elif MEAN == MEDIAN and MEAN * 2 == MIN + MAX:
        print(f"Case #{t + 1}: 2")
    else:
        # Odd number case, MIN, ..., MEDIAN, ..., MAX
        diff = MIN + MAX + MEDIAN - MEAN * 3
        if diff == 0:
            odd_ans = 3
        else:
            if diff < 0: # Current mean is smaller than target mean
                diff = -diff
                # Insert a pair of MIN and MEDIAN can reduce the mean difference by temp, then calculate how many pairs we need to insert
                temp = MAX + MEDIAN - MEAN * 2
            else: # Current mean is bigger than target mean
                temp = MEAN * 2 - MIN - MEDIAN
            if temp <= 0: # Never can adjust the current mean to target
                odd_ans = INF
            else:
                odd_ans = ((diff - 1) // temp + 1) * 2 + 3

        # Even number case, MIN, ..., MEDIAN, MEDIAN, ..., MAX
        diff = MIN + MAX + MEDIAN + MEDIAN - MEAN * 4
        if diff == 0:
            even_ans = 4
        else:
            if diff < 0:
                diff = -diff
                temp = MAX + MEDIAN - MEAN * 2
            else:
                temp = MEAN * 2 - MIN - MEDIAN
            if temp <= 0:
                even_ans = INF
            else:
                even_ans = ((diff - 1) // temp + 1) * 2 + 4

        if odd_ans == INF and even_ans == INF:
            print(f"Case #{t + 1}: IMPOSSIBLE")
        else:
            print(f"Case #{t + 1}: {min(odd_ans, even_ans)}")
