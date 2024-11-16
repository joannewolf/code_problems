#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'equal' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def equal(arr):
    INT_MAX = 10000000
    min_num = min(arr)
    targets = [min_num - i for i in range(5)] # possible targets
    result = INT_MAX
    for target in targets:
        new_arr = [num - target for num in arr]
        count = 0
        for num in new_arr:
            count += num // 5
            num %= 5
            count += num // 2
            num %= 2
            count += num // 1
        result = min(result, count)

    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = equal(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
