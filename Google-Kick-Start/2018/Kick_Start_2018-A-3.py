# Scrambled Words
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050edf/0000000000051004
# O(NL), TLE on test set 2

ascii_a = ord('a')

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

    starts = {}
    for i in range(26):
        starts[chr(ascii_a + i)] = []
    letters = [[0] for _ in range(26)]
    for i in range(N):
        starts[S[i]].append(i)
        for j in range(26):
            letters[j].append(letters[j][-1])
        letters[ord(S[i]) - ascii_a][-1] += 1
    # for c in starts:
    #     print(c, starts[c])
    # for i in range(26):
    #     print(letters[i])

    ans = 0
    for word in words:
        n = len(word)
        for s in starts[word[0]]:
            if s + n - 1 < N and S[s + n - 1] == word[-1]: # First and last letter are same
                match_all = True
                word_letters = [0] * 26
                for c in word:
                    word_letters[ord(c) - ascii_a] += 1
                for i in range(26):
                    if word_letters[i] != letters[i][s + n] - letters[i][s]:
                        match_all = False
                        break
                if match_all:
                    # print(word, word_letters, "s", s)
                    ans += 1
                    break

    print(f"Case #{t + 1}: {ans}")
