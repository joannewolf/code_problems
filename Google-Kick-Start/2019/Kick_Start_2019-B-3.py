# Diverse Subarray
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050eda/00000000001198c1
# Brute-Force O(N^2*A), TLE on test set 1

T = int(input())
for t in range(T):
    [N, S] = [int(n) for n in input().split()]
    types = [int(n) for n in input().split()]

    prefix_map = [{}]
    for type in types:
        new_map = prefix_map[-1].copy()
        if type in new_map:
            new_map[type] += 1
        else:
            new_map[type] = 1
        prefix_map.append(new_map)

    ans = 0
    for l in range(N):
        for r in range(l + 1, N + 1):
            count = 0
            for type in prefix_map[r]:
                if type in prefix_map[l]:
                    num = prefix_map[r][type] - prefix_map[l][type]
                else:
                    num = prefix_map[r][type]
                if num > S:
                    num = 0
                count += num
            ans = max(ans, count)

    print(f"Case #{t + 1}: {ans}")
