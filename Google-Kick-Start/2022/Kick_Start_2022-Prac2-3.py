# Building Palindromes
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000008f4a94/0000000000b54d3b

from pprint import pprint

ascii_A = ord('A')

T = int(input())
for t in range(T):
    [N, Q] = [int(x) for x in input().split()]
    S = input()

    prefix_letters = []
    prefix_letters.append([0] * 26)
    for i in range(N):
        next = prefix_letters[-1].copy()
        next[ord(S[i]) - ascii_A] += 1
        prefix_letters.append(next)
    # pprint(prefix_letters)

    ans = 0
    for i in range(Q):
        [L, R] = [int(x) for x in input().split()]
        odd = False
        valid = True
        for j in range(26):
            curr_letter_num = prefix_letters[R][j] - prefix_letters[L-1][j]
            if curr_letter_num % 2 == 0:
                continue
            elif curr_letter_num % 2 == 1 and not odd:
                odd = True
            else:
                valid = False
                break
        if valid:
            ans += 1

    print(f"Case #{t + 1}: {ans}")
