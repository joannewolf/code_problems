# Diverse Subarray
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050eda/00000000001198c1
# Consider a fix left point l, transfer the type list to score list and find max prefix sum
# For each type of trinkets, the 1~Sth occurrence can get +1 score, the S+1th occurrence get -S score, the S+2th occurrence and after get +0 score
# For each left point it takes O(N), and there are N left points, O(N^2), TLE on test set 2

T = int(input())
for t in range(T):
    [N, S] = [int(n) for n in input().split()]
    types = [int(n) for n in input().split()]

    ans = 0
    for l in range(N):
        type_map = {}
        scores = []
        for type in types[l:]:
            if type not in type_map:
                scores.append(1)
                type_map[type] = 1
            elif type_map[type] < S:
                scores.append(1)
                type_map[type] += 1
            elif type_map[type] == S:
                scores.append(-S)
                type_map[type] += 1
            elif type_map[type] > S:
                scores.append(0)
                type_map[type] += 1
        sum = 0
        for score in scores:
            sum += score
            ans = max(ans, sum)

    print(f"Case #{t + 1}: {ans}")
