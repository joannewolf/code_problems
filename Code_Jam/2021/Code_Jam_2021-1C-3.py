# Double or NOTing
# https://codingcompetitions.withgoogle.com/codejam/round/00000000004362d7/00000000007c1139
# mark consecutive 0 or 1 as a group
# NOT action can eliminate one group from S, DOUBLE action can add one digit at the end
# To construct E, we can reuse 0 or some suffix from S as prefix, and use DOUBLE actions to fill the remaining digits
# If # NOT to eliminate S prefix >= # NOT to create remaining digit group, then it's a valid sequence

import math

MAX_INT = 300

T = int(input())
for t in range(T):
    [S, E] = input().split()

    group_S = []
    flag = S[0]
    count = 0
    for c in S:
        if c == flag:
            count += 1
        else:
            group_S.append(count)
            flag = c
            count = 1
    group_S.append(count)

    group_E = []
    flag = E[0]
    count = 0
    for c in E:
        if c == flag:
            count += 1
        else:
            group_E.append(count)
            flag = c
            count = 1
    group_E.append(count)

    # print(group_S)
    # print(group_E)

    result = MAX_INT
    if S == '0' and E == '0':
        result = 0
    elif S[0] == '1' and E == '0':
        result = len(group_S)
    elif S == '0' and group_E[0] == 1 and len(group_E) < 3:
        result = sum(group_E)
    elif S == '0' and len(group_E) < 3:
        result = sum(group_E) + 2
    elif S[0] == '1' and E[0] == '1':
        # If eliminate i groups from S
        for i in range(0, len(group_S) + 1):
            # print(f"i: {i}")
            # If S's suffix can be E's prefix
            if len(group_S)-i <= len(group_E):
                step = MAX_INT
                # Not reuse any bit from S
                if len(group_S)-i == 0 and i >= len(group_E):
                    step = i + sum(group_E)
                    # print(f"step1: {step}")
                # Reuse last group from S but not able to fill first E group, if S ends with 0, it needs one less NOT to fill the remaining bits
                elif group_S[i:-1] == group_E[0:len(group_S)-i-1] and group_S[-1] < group_E[len(group_S)-i-1] and i >= len(group_E) - (len(group_S)-i-1) - (len(group_S) % 2 == 0):
                    step = i + (group_E[len(group_S)-i-1] - group_S[-1]) + sum(group_E[len(group_S)-i:])
                    # print(f"step2: {step}")
                # Reuse last group from S and able to fill first E group, if S ends with 1, it needs one less NOT to fill the remaining bits
                elif group_S[i:] == group_E[0:len(group_S)-i] and i >= len(group_E) - (len(group_S)-i) - (len(group_S) % 2 == 1):
                    step = i + sum(group_E[len(group_S)-i:])
                    # print(f"step3: {step}")

                if step < result:
                    result = step

    if result == MAX_INT:
        print(f"Case #{t + 1}: IMPOSSIBLE")
    else:
        print(f"Case #{t + 1}: {result}")
