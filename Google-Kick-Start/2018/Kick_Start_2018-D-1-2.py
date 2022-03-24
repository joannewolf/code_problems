# Candies
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050ee1/00000000000510ef
# Key idea: If for l', r' is the rightmost index which satisfying odd[l', r'] <= O, then odd[l'+1, r'] <= O must also satisfy
# For test set 1 only, L = 0, all Si >= 0, if r' also satisfying sum[l', r'] <= D, sum[l'+1, r'] <= D must also satisfy

N_INF = -pow(10, 15) - 1

T = int(input())
for t in range(T):
    [N, O, D] = [int(x) for x in input().split()]
    [X1, X2, A, B, C, M, L] = [int(x) for x in input().split()]
    S = [X1, X2]
    for i in range(2, N):
        next = (S[-1] * A + S[-2] * B + C) % M
        S.append(next)
    for i in range(N):
        S[i] += L
    # print(S)

    sum = [0]
    odd = [0]
    for i in range(N):
        sum.append(sum[-1] + S[i])
        odd.append(odd[-1] + (S[i] % 2))
    # print(sum)

    ans = N_INF

    # O(N), Only handle test set 1, L = 0 -> all Si >= 0
    # For each l, the rightmost index which satisfying constraints will always give maximized sum
    # So for next l, we can start iterate from last rightmost index
    # flag_r = 0
    # for l in range(N):
    #     for r in range(flag_r, N+1):
    #         if r == N or odd[r+1] - odd[l] > O or sum[r+1] - sum[l] > D:
    #             flag_r = r
    #             break
    #     if flag_r > l and sum[flag_r] - sum[l] > ans:
    #         ans = sum[flag_r] - sum[l]

    # For test set 2, instead of directly taking the rightmost index, we search all candidates within rightmost index and get the one which satifying sum[l, r'] <= D
    # We need a data structure for candidates, it should support adding int, removing int, and finding the max int which <= target
    # Binary search tree can do it, O(NlogN)
    flag_r = 0
    candidates = []
    for l in range(N):
        for r in range(max(l, flag_r), N+1):
            if r == N or odd[r+1] - odd[l] > O:
                flag_r = r
                break
            else:
                candidates.append(sum[r+1])

        # Find max candidate - sum[l] <= D
        candidates.sort()
        l2, r2 = 0, len(candidates) - 1
        while l2 <= r2:
            mid = (l2 + r2) // 2
            if candidates[mid] <= D + sum[l]:
                l2 = mid + 1
            else:
                r2 = mid - 1
        if r2 >= 0 and candidates[r2] - sum[l] > ans:
            ans = candidates[r2] - sum[l]

        if sum[l+1] in candidates:
            candidates.remove(sum[l+1])

    if ans == N_INF:
        print(f"Case #{t + 1}: IMPOSSIBLE")
    else:
        print(f"Case #{t + 1}: {ans}")
