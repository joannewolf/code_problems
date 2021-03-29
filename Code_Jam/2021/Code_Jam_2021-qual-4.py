# Median Sort
# https://codingcompetitions.withgoogle.com/codejam/round/000000000043580a/00000000006d1284
# Get all combination(N, 3) and ask for median, starting from head and tail number since they never be median, and so on until the middle number
# In second round, to decide which one is next to the first head, test with (first head, second head, second tail) and find who is median
# Pass test set 1

import sys
import statistics

[T, N, Q] = [int(n) for n in input().split()]
for t in range(T):
    medians = {}
    for i in range(N):
        for j in range(i + 1, N):
            for k in range(j + 1, N):
                print("{} {} {}".format(i + 1, j + 1, k + 1))
                sys.stdout.flush()
                medians[(i + 1, j + 1, k + 1)] = int(input())
    # print(medians)

    nums = [0] * N
    remain_num = set(range(1, N + 1))
    remain_medians = medians.copy()
    for i in range((N + 1) // 2):
        candidate = remain_num.copy()
        for k, v in remain_medians.items():
            candidate.discard(v)
        candidate = list(candidate)
        # print("candidate", candidate)
        if i == 0:
            nums[0] = candidate[0]
            nums[-1] = candidate[1]
        elif len(candidate) == 1:
            nums[i] = candidate[0]
            break
        elif len(candidate) == 2:
            temp = sorted(candidate + [nums[i - 1]])
            # Find which candidate should be next to last round of head
            if (medians[(temp[0], temp[1], temp[2])] == candidate[0]):
                nums[i] = candidate[0]
                nums[-1 - i] = candidate[1]
            elif (medians[(temp[0], temp[1], temp[2])] == candidate[1]):
                nums[i] = candidate[1]
                nums[-1 - i] = candidate[0]
        
        remain_num.discard(candidate[0])
        remain_num.discard(candidate[1])
        for key in [k for k in remain_medians.keys() if (candidate[0] in k or candidate[1] in k)]:
            del remain_medians[key]

    print(' '.join(str(i) for i in nums))
    sys.stdout.flush()
    result = input()
    if result == '1':
        continue
    else:
        sys.exit()
