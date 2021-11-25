# Circuit Board
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050ff2/0000000000150aae
# The problem can be divided into 2 subproblems
# Subproblem 1: For each starting point (r, c), find the max length to its right side such that max-and-min-element-diff <= K
#   Subproblem 1.1: Get range minimum and maximum for each row, which can be achieved by using sparse table, pre-processing O(ClogC) for each row, query O(1) => total O(RClogC)
#   Subproblem 1.2: Use binary search to find the max index such that max-and-min-element-diff <= K, O(logC) for each (r, c) => total O(RClogC)
#       Since max-and-min-element-diff is non-decreasing when it goes to array's right side
# Subproblem 2: For each starting column j, we have the max length for each row, find the largest rectangle of histogram
#   For each num, take it as height of rectangle, and look for the furthest left/right index it can reach
# O(R) for each column => total O(RC)
# Overall O(RClogC)

import math

T = int(input())
for t in range(T):
    [R, C, K] = [int(n) for n in input().split()]
    board = []
    for _ in range(R):
        row = [int(n) for n in input().split()]
        board.append(row)

    histogram = [[0] * C for i in range(R)] # histogram[i][j]: on row i, the max length to board[i][j]'s right side such that max-and-min-element-diff <= K

    LOG_C = math.floor(math.log2(C))
    for r in range(R):
        # Subproblem 1.1 For each row, pre-process sparse tables for range min/max
        sparse_min = [[0] * (LOG_C+1) for _ in range(C)]
        sparse_max = [[0] * (LOG_C+1) for _ in range(C)]
        for c in range(C):
            sparse_min[c][0] = board[r][c]
            sparse_max[c][0] = board[r][c]
        for j in range(1, LOG_C+1):
            for i in range(C - pow(2, j-1)):
                sparse_min[i][j] = min(sparse_min[i][j-1], sparse_min[i + pow(2, j-1)][j-1])
                sparse_max[i][j] = max(sparse_max[i][j-1], sparse_max[i + pow(2, j-1)][j-1])
        # Subproblem 1.2
        for c in range(C):
            left, right = c, C - 1
            while left <= right:
                mid = (left + right) // 2
                k = math.floor(math.log2(mid - c + 1))
                range_min = min(sparse_min[c][k], sparse_min[mid - pow(2, k) + 1][k])
                range_max = max(sparse_max[c][k], sparse_max[mid - pow(2, k) + 1][k])
                if range_max - range_min <= K:
                    left = mid + 1
                else:
                    right = mid - 1
            # Final r is max element index which <= K
            histogram[r][c] = right - c + 1
    
    # Subproblem 2
    ans = 0
    for c in range(C):
        left_bound = [-1] * R
        right_bound = [-1] * R
        stack = []

        # Find every num's right bound
        for r in range(R):
            while stack and histogram[stack[-1]][c] > histogram[r][c]:
                right_bound[stack[-1]] = r - 1
                stack.pop(-1)
            stack.append(r)
        while stack:
            right_bound[stack[-1]] = R - 1
            stack.pop(-1)

        # Find every num's left bound
        for r in range(R-1, -1, -1):
            while stack and histogram[stack[-1]][c] > histogram[r][c]:
                left_bound[stack[-1]] = r + 1
                stack.pop(-1)
            stack.append(r)
        while stack:
            left_bound[stack[-1]] = 0
            stack.pop(-1)

        for r in range(R):
            ans = max(ans, histogram[r][c] * (right_bound[r] - left_bound[r] + 1))

    print(f"Case #{t + 1}: {ans}")
