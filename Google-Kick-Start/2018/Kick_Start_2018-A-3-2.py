# Scrambled Words
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050edf/0000000000051004
# "The sum of lengths of all words in the dictionary does not exceed 10^5.", let M = 10^5
# The # of distinct word length = O(sqrt(M))
# O(Nsqrt(M)), TLE but correct locally on test set 2

ascii_a = ord('a')

def add_map(map: map, key: tuple):
    if key not in map:
        map[key] = 1
    else:
        map[key] += 1

T = int(input())
for t in range(T):
    L = int(input())
    words = input().split()
    [S1, S2, N, A, B, C, D] = input().split()
    S = [S1, S2]
    N = int(N)
    A = int(A)
    B = int(B)
    C = int(C)
    D = int(D)
    x1 = ord(S1)
    x2 = ord(S2)
    for i in range(2, N):
        x3 = (A * x2 + B * x1 + C) % D
        # print(x1, x2, x3)
        S.append(chr(ord('a') + x3 % 26))
        x1, x2 = x2, x3
    # print("".join(S))

    dict = {}
    word_len = set()
    for word in words:
        word_len.add(len(word))
        word_letters = [0] * 26
        for c in word:
            word_letters[ord(c) - ascii_a] += 1
        add_map(dict, (word[0], word[-1], tuple(word_letters)))

    ans = 0
    # For each distinct word length, maintain a running letter frequency list against main string S
    for n in word_len:
        # Construct initial string
        letters = [0] * 26
        st = S[0]
        ed = S[n - 1]
        for i in range(n):
            letters[ord(S[i]) - ascii_a] += 1
        if (st, ed, tuple(letters)) in dict:
            ans += dict.pop( (st, ed, tuple(letters)) )
        # Sliding the string
        for flag in range(n, N):
            letters[ord(S[flag - n]) - ascii_a] -= 1
            letters[ord(S[flag]) - ascii_a] += 1
            st = S[flag - n + 1]
            ed = S[flag]
            if (st, ed, tuple(letters)) in dict:
                ans += dict.pop( (st, ed, tuple(letters)) )

    print(f"Case #{t + 1}: {ans}")
