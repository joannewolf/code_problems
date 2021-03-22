# Indicium
# https://codingcompetitions.withgoogle.com/codejam/round/000000000019fd27/0000000000209aa0

def find_two_combination(sum, candidate):
    ans = []
    for i in range(len(candidate)):
        for j in range(i, len(candidate)):
            if candidate[i] + candidate[j] == sum:
                ans.append([candidate[i], candidate[j]])
    return ans

T = int(raw_input())
for t in xrange(T):
    N, K = [int(x) for x in raw_input().split(' ')]

    # the impossible case is when K can only be constructed by pattern AA..AB, cuz the last A can only be put at B's location
    # greedily get trace in pattern AA..ABC, A != B, A != C, B can be == C
    # edge case: if N == 2, A doesn't exist, B has to == C; if N == 3, B has to != C
    all_combination = [] 
    for i in range(1, N + 1):
        if i * (N - 2) < K:
            if i * N == K:
                all_combination.insert(0, [i, i, i])
            candidate = range(1, N + 1)
            candidate.remove(i)
            candidate = filter(lambda num: num < K - i * (N - 2), candidate)
            temp_ans = find_two_combination(K - i * (N - 2), candidate)
            for combination in temp_ans:
                combination.insert(0, i)
                all_combination.append(combination)

    if not all_combination:
        print "Case #{}: IMPOSSIBLE".format(t + 1)
        continue
    elif N == 3 and set([comb[0] != comb[-1] and comb[-2] == comb[-1] for comb in all_combination]) == set([True]):
        print "Case #{}: IMPOSSIBLE".format(t + 1)
        continue
    else:
        print "Case #{}: POSSIBLE".format(t + 1)
        ans = []
        # if A == B && B == C, construct a base [A, ...] and use it to create a circulant Latin square
        if all_combination[0][0] == all_combination[0][1] and all_combination[0][1] == all_combination[0][2]:
            base = [all_combination[0][0]]
            remain_num = range(1, N + 1)
            remain_num.remove(all_combination[0][0])
            base.extend(remain_num)
            for i in range(0, N):
                ans.append(base[-i:] + base[0: -i])
        # if A != B && A != C && B != C, construct a base [A, B, ..., C] and use it to create a circulant Latin square
        # but the last two rows need to be reversed, like:
        # A, B, ..., C
        # ...
        # ..., C, A, B -> B, ..., C, A
        # B, ..., C, A -> ..., C, A, B
        elif all_combination[0][1] != all_combination[0][2]:
            base = [all_combination[0][0], all_combination[0][1]]
            remain_num = [num for num in range(1, N + 1) if num not in all_combination[0]]
            base.extend(remain_num)
            base.append(all_combination[0][2])
            for i in range(0, N):
                ans.append(base[-i:] + base[0: -i])
            temp = ans[N - 2]
            ans[N - 2] = ans[N - 1]
            ans[N - 1] = temp
        # if A != B && B == C, construct a base [A, B, ...] and use it to create a circulant Latin square
        # but the last three rows need to be adjusted, like:
        # [remain]: n1, n2, ...
        # A, B, X,   [remain]   , Y
        # ...
        # B,   [remain]   , A, Y, X
        # n1, n3, n2, n4, ..., B, A
        # n2, n1, n4, n3, ..., A, B
        else:
            base = [all_combination[0][0], all_combination[0][1]]
            remain_num = [num for num in range(1, N + 1) if num not in all_combination[0]]
            base.extend(remain_num)
            for i in range(0, N - 3):
                ans.append(base[-i:] + base[0: -i])
            
            ans.append([all_combination[0][1]] + remain_num[1: -1] + [all_combination[0][0], remain_num[-1], remain_num[0]])
            
            second_last_row = [remain_num[0]]
            for i in range((len(remain_num) - 1) / 2):
                second_last_row += [remain_num[2 * i + 2], remain_num[2 * i + 1]]
            if len(remain_num) % 2 == 0:
                second_last_row += [remain_num[-1]]
            ans.append(second_last_row + [all_combination[0][1], all_combination[0][0]])
            
            last_row = []
            for i in range(len(remain_num) / 2):
                last_row += [remain_num[2 * i + 1], remain_num[2 * i]]
            if len(remain_num) % 2 == 1:
                last_row += [remain_num[-1]]
            ans.append(last_row + [all_combination[0][0], all_combination[0][1]])

        for row in ans:
            print " ".join(map(str,row))
