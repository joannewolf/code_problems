# Staying Hydrated
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000004362d6/00000000008b3a1c

import sys
import math

T = int(input())
for t in range(T):
    K = int(input())
    x_start = []
    x_end = []
    y_start = []
    y_end = []
    for i in range(K):
        [x1, y1, x2, y2] = [int(n) for n in input().split()]
        x_start.append(x1)
        x_end.append(x2)
        y_start.append(y1)
        y_end.append(y2)

    x_start.sort()
    x_end.sort()
    y_start.sort()
    y_end.sort()

    # If furniture_right > furniture_left, then moving one step right can reduce total distance
    # Until we cannot further optimize
    furniture_right = K
    furniture_left = 0
    flag_start = 0
    flag_end = 0
    min_x = -pow(10, 9)
    while flag_start < K or flag_end < K:
        if x_start[flag_start] < x_end[flag_end]:
            furniture_right -= 1
            min_x = x_start[flag_start]
            flag_start += 1
        else:
            furniture_left += 1
            min_x = x_end[flag_end]
            flag_end += 1
        if furniture_right - furniture_left <= 0:
            break

    furniture_up = K
    furniture_down = 0
    flag_start = 0
    flag_end = 0
    min_y = -pow(10, 9)
    while flag_start < K or flag_end < K:
        if y_start[flag_start] < y_end[flag_end]:
            furniture_up -= 1
            min_y = y_start[flag_start]
            flag_start += 1
        else:
            furniture_down += 1
            min_y = y_end[flag_end]
            flag_end += 1
        if furniture_up - furniture_down <= 0:
            break

    print(f"Case #{t + 1}: {min_x} {min_y}")
