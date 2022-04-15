# Pattern Overlap
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000201c97/0000000000201b79
# Using dp, O(N1 * N2)

def solve(flag1, flag2):
    # print("flag1", flag1, S1[flag1:], "flag2", flag2, S2[flag2:])
    if match[flag1][flag2] != -1:
        return match[flag1][flag2]

    if flag1 == N1:
        valid = True
        for i in range(flag2, N2):
            if S2[i] != '*':
                valid = False
                break
        for i in range(flag2, N2):
            match[flag1][i] = valid

    elif flag2 == N2:
        valid = True
        for i in range(flag1, N1):
            if S1[i] != '*':
                valid = False
                break
        for i in range(flag1, N1):
            match[i][flag2] = valid

    elif S1[flag1] != '*' and S2[flag2] != '*':
        if S1[flag1] == S2[flag2]:
            match[flag1][flag2] = solve(flag1 + 1, flag2 + 1)
        else:
            match[flag1][flag2] = False
    else:
        res = False
        if S1[flag1] == '*':
            count_c2 = 0
            for i in range(flag2, N2+1):
                if count_c2 <= 4:
                    # print("i", i, "count_c2", count_c2, S1[flag1+1:], S2[i:])
                    res |= solve(flag1 + 1, i)
                    if res:
                        match[flag1][flag2] = res
                        break
                else:
                    break
                if i != N2 and S2[i] != '*':
                    count_c2 += 1
        if S2[flag2] == '*':
            count_c1 = 0
            for i in range(flag1, N1+1):
                if count_c1 <= 4:
                    # print("i", i, "count_c1", count_c1, S1[i:], S2[flag2+1:])
                    res |= solve(i, flag2 + 1)
                    if res:
                        match[flag1][flag2] = res
                        break
                else:
                    break
                if i != N1 and S1[i] != '*':
                    count_c1 += 1
        match[flag1][flag2] = res

    return match[flag1][flag2]

T = int(input())
for t in range(T):
    S1 = input()
    S2 = input()
    N1 = len(S1)
    N2 = len(S2)

    match = [[-1] * (N2+1) for _ in range(N1+1)]
    # match[i][j]: Whether S1[i:] and S2[j:] are matching pattern
    match[N1][N2] = True

    solve(0, 0)

    if match[0][0]:
        print(f"Case #{t + 1}: TRUE")
    else:
        print(f"Case #{t + 1}: FALSE")
