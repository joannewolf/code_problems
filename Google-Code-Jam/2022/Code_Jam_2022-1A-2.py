# Equal Sum
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000877ba5/0000000000aa8fc1
# Key idea: if we sort out the numbers into two sets, trying for their sums to be as close as possible
# The max difference is bounded by a single number size, i.e. at most 10^9; log2(10^9) = 29.xx, 

import sys
import random

pow2 = [pow(2, i) for i in range(29, -1, -1)]
MAX_INT = pow(10, 9)

T = int(input())
for t in range(T):
    N = int(input())

    pool = random.sample(range(1, MAX_INT), 2 * N)
    pool = list(filter(lambda x: x not in pow2, pool))
    numsA = random.sample(pool, N - 30)
    print(f"{' '.join(map(str, pow2 + numsA))}")
    sys.stdout.flush()

    numsB = [int(x) for x in input().split()]

    sum1 = 0
    sum2 = 0
    set1 = []
    set2 = []
    for num in numsA + numsB + pow2:
        if sum1 <= sum2:
            set1.append(num)
            sum1 += num
        else:
            set2.append(num)
            sum2 += num

    # print(sum1, set1)
    # print(sum2, set2)
    print(f"{' '.join(map(str, set1))}")
    sys.stdout.flush()
