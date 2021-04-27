# Digit Blocks
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000435baf/00000000007ae37b
# Greedily only put digit 9 (or 8) in the most top position, pass test set 1
# Adding limit on 8 and 7, sometimes pass test set 2

import sys

[T, N, B, P] = [int(n) for n in input().split()]
for t in range(T):
    blocks = [0] * N

    for i in range(N * B):
        D = int(input())
        if D == 9:
            next_candidate = -1
            for i in range(N):
                if blocks[i] == B - 1:
                    next_candidate = i + 1
                    break
                elif blocks[i] != B and next_candidate == -1:
                    next_candidate = i + 1
        elif D == 8 or (D == 7 and i > N * B * 2 // 3):
            next_candidate = -1
            for i in range(N):
                if blocks[i] < B - 1:
                    next_candidate = i + 1
                    break
                elif blocks[i] != B and next_candidate == -1:
                    next_candidate = i + 1
        else:
            next_candidate = -1
            for i in range(N):
                if blocks[i] < B - 2:
                    next_candidate = i + 1
                    break
                elif blocks[i] != B and next_candidate == -1:
                    next_candidate = i + 1
        blocks[next_candidate - 1] += 1
        print(next_candidate)
        sys.stdout.flush()

result = int(input())