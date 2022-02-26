# Code-Eat Switcher
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050edb/00000000001707b8
# Key idea: to achieve 1 unit time of eating, we're losing C/E unit of coding
# So if Ci/Ei <= Cj/Ej, it's better to choose slot i to eat
# -> sort slots by C/E, and use that order to achieve eating time

T = int(input())
for t in range(T):
    [D, S] = [int(n) for n in input().split()]
    slots = []
    for _ in range(S):
        [C, E] = [int(n) for n in input().split()]
        slots.append((C, E))

    slots.sort(key=lambda x: x[0] / x[1])
    prefix_eating_sum = [slots[0][1]]
    suffix_coding_sum = [slots[-1][0]]
    for i in range(1, S):
        prefix_eating_sum.append(prefix_eating_sum[-1] + slots[i][1])
        suffix_coding_sum.append(suffix_coding_sum[-1] + slots[S - 1 - i][0])
    suffix_coding_sum.reverse()
    # for (c, e) in slots:
    #     print(c, e, c/e)
    # print(prefix_eating_sum)
    # print(suffix_coding_sum)

    ans = ""
    for _ in range(D):
        [A, B] = [int(n) for n in input().split()]
        # Final L is the first index where prefix_eating_sum[i] >= B
        l, r = 0, S - 1
        while l <= r:
            mid = (l + r) // 2
            if prefix_eating_sum[mid] < B:
                l = mid + 1
            else:
                r = mid - 1
        # print("L", l)
        if l == S:
            ans += "N"
        else:
            coding_time = (prefix_eating_sum[l] - B) * slots[l][0] / slots[l][1]
            if l != S - 1:
                coding_time += suffix_coding_sum[l + 1]
            # print(prefix_eating_sum[l] - B, slots[l], suffix_coding_sum[l + 1])
            if coding_time >= A:
                ans += "Y"
            else:
                ans += "N"

    print(f"Case #{t + 1}: {ans}")
