# Lucky Dip
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050edf/0000000000050e1d
# Define E[i]: expected value when K = i
# E[0] = SUM{V} / N; E[1] = max(V, E[0]) / N, keep it if the value is larger than the expected value of redip
# O(NK), TLE on test set 2

T = int(input())
for t in range(T):
    [N, K] = [int(x) for x in input().split()]
    values = [int(x) for x in input().split()]

    E = 0
    for i in range(K + 1):
        temp = 0
        for v in values:
            temp += max(v, E)
        E = temp / N

    print(f"Case #{t + 1}: {E}")
