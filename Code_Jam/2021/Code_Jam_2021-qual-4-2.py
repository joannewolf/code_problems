# Median Sort
# https://codingcompetitions.withgoogle.com/codejam/round/000000000043580a/00000000006d1284

import sys

def ask(a, b, c):
    print("{} {} {}".format(a, b, c))
    sys.stdout.flush()
    return int(input())

[T, N, Q] = [int(n) for n in input().split()]
for t in range(T):
    nums = []
    # Initialization, add fake head and tail
    first_median = ask(1, 2, 3)
    if (first_median == 1):
        nums = [-1, 2, 1, 3, -1]
    elif (first_median == 2):
        nums = [-1, 1, 2, 3, -1]
    else:
        nums = [-1, 1, 3, 2, -1]

    # Insert new num by finding its position using binary search
    for i in range(4, N + 1):
        l = 0
        r = len(nums) - 1
        while (r - l > 1):
            if (r - l >= 3 or (l != 0 and r != len(nums) - 1)):
                mid1 = (2 * l + r) // 3
                mid2 = (l + 2 * r) // 3
                median = ask(i, nums[mid1], nums[mid2])
                if (median == i):
                    l = mid1
                    r = mid2
                elif (median == nums[mid1]):
                    r = mid1
                else:
                    l = mid2
            elif (l == 0):
                median = ask(i, nums[1], nums[2])
                if (median == nums[1]):
                    r = 1
                else:
                    l = 1
            elif (r == len(nums) - 1):
                median = ask(i, nums[-2], nums[-3])
                if (median == nums[-2]):
                    l = len(nums) - 2
                else:
                    r = len(nums) - 2
        # i should be inserted between l and r
        nums = nums[:l + 1] + [i] + nums[r:]

    print(' '.join(str(i) for i in nums[1:-1]))
    sys.stdout.flush()
    result = input()
    if result == '1':
        continue
    else:
        sys.exit()
