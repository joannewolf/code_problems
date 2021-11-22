# Building Palindromes
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050eda/0000000000119866

T = int(input())
for t in range(T):
    [N, Q] = [int(n) for n in input().split()]
    letters = input()

    prefix_map = [{}]
    for c in letters:
        new_map = prefix_map[-1].copy()
        if c in new_map:
            new_map[c] += 1
        else:
            new_map[c] = 1
        prefix_map.append(new_map)
    # print(prefix_map)

    ans = 0
    for i in range(Q):
        [l, r] = [int(n) for n in input().split()]
        odd_char = 0
        for c in prefix_map[r]:
            if c in prefix_map[l - 1]:
                char_num = prefix_map[r][c] - prefix_map[l - 1][c]
            else:
                char_num = prefix_map[r][c]
            if char_num % 2 == 1:
                odd_char += 1
            if odd_char > 1:
                break
        ans += (odd_char <= 1)

    print(f"Case #{t + 1}: {ans}")
