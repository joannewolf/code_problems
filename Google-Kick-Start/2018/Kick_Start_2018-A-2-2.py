# Lucky Dip
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050edf/0000000000050e1d
# Define E[i]: expected value when K = i
# E[0] = SUM{V} / N; E[1] = max(V, E[0]) / N, keep it if the value is larger than the expected value of redip
# O(NlogN + N + KlogN) = O((N+K)logN)

T = int(input())
for t in range(T):
    [N, K] = [int(x) for x in input().split()]
    values = [int(x) for x in input().split()]
    values.sort()

    suffix_sum = [0]
    for i in range(N - 1, -1, -1):
        suffix_sum.append(suffix_sum[-1] + values[i])
    suffix_sum.reverse()
    # print(suffix_sum)

    E = 0
    for i in range(K + 1):
        # Find the first value which >= current E, i.e. final L
        l, r = 0, N - 1
        while l <= r:
            mid = (l + r) // 2
            if values[mid] < E:
                l = mid + 1
            else:
                r = mid - 1
        # print(l, r)
        E = (E * l + suffix_sum[l]) / N

    print(f"Case #{t + 1}: {E}")
