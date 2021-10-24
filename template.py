# 
# https://codingcompetitions.withgoogle.com/

import sys
import math

T = int(input())
for t in range(T):

    A = [int(n) for n in input().split()]
    matrix_2d = [[0] * C for i in range(R)]
    matrix_3d = [[[0] * N for j in range(N)] for i in range(N)]

    # print("{} {} {}".format(i + 1, j + 1, k + 1))
    # sys.stdout.flush()

    ans = 0

    print(f"Case #{t + 1}: {ans}")
    # print(f"Case #{t + 1}: {' '.join([str(n) for n in ans])}")
