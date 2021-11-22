# Festival
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435bae/0000000000887dba
# O(N * N), TLE on test set 2

T = int(input())
for t in range(T):
    [D, N, K] = [int(n) for n in input().split()]
    attraction_start = []
    attraction_end = []
    for i in range(N):
        [h, s, e] = [int(n) for n in input().split()]
        attraction_start.append((s, h))
        attraction_end.append((e, h))
    attraction_start.sort()
    attraction_end.sort()
    # print(attraction_start)
    # print(attraction_end)

    result = 0
    available_first_K = []
    available_rest = []
    # If use 2 multiset to store first K and rest attractions, can achieve O(N * logN)
    flag_start = 0
    flag_end = 0
    while flag_start < N or flag_end < N:
        if flag_start == N or attraction_start[flag_start][0] > attraction_end[flag_end][0]:
            # Remove attraction from available list
            current = attraction_end[flag_end][1]
            if current in available_first_K:
                available_first_K.remove(current)
                if available_rest:
                    available_first_K.append(max(available_rest))
                    available_rest.remove(max(available_rest))
            else:
                available_rest.remove(current)
            flag_end += 1
        else:
            # Add attraction to available list
            current = attraction_start[flag_start][1]
            if len(available_first_K) < K:
                available_first_K.append(current)
            else:
                if min(available_first_K) >= current:
                    available_rest.append(current)
                else:
                    available_first_K.append(current)
                    available_rest.append(min(available_first_K))
                    available_first_K.remove(min(available_first_K))
            flag_start += 1

        if sum(available_first_K) > result:
            result = sum(available_first_K)

    print(f"Case #{t + 1}: {result}")
