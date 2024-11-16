#!/bin/python3

import math
import os
import random
import re
import sys
from tabnanny import check

#
# Complete the 'lilysHomework' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def lilysHomework(arr):
    # Write your code here
    N = len(arr)
    sorted_arr1 = sorted(arr)
    sorted_arr2 = sorted(arr, reverse=True)
    old_index = {val: i for i, val in enumerate(arr)}

    # compare with sorted_arr1
    count1 = 0
    checked = set()
    for i in range(N):
        if arr[i] not in checked:
            checked.add(arr[i])
            current = sorted_arr1[i]
            while arr[i] != current:
                checked.add(current)
                current = sorted_arr1[old_index[current]]
                count1 += 1

    # compare with sorted_arr2
    count2 = 0
    checked = set()
    for i in range(N):
        if arr[i] not in checked:
            checked.add(arr[i])
            current = sorted_arr2[i]
            while arr[i] != current:
                checked.add(current)
                current = sorted_arr2[old_index[current]]
                count2 += 1

    return min(count1, count2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = lilysHomework(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
