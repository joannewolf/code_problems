# 
# https://codingcompetitions.withgoogle.com/

import sys
import math

T = int(input())
for t in range(T):

    A = [int(x) for x in input().split()]
    matrix_2d = [[0] * C for _ in range(R)]
    matrix_3d = [[[0] * N for _ in range(N)] for _ in range(N)]

    # print("{} {} {}".format(i + 1, j + 1, k + 1))
    # sys.stdout.flush()

    ans = 0

    print(f"Case #{t + 1}: {ans}")
    # print(f"Case #{t + 1}: {' '.join(map(str, ans))}")
    # print("bits", format(bits, f'#0{n+2}b'))
