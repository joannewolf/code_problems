# Ambiguous Cipher
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000201c98/0000000000201d26

T = int(input())
for t in range(T):
    word = input()
    N = len(word)

    if N % 2 == 1:
        print(f"Case #{t + 1}: AMBIGUOUS")
    else:
        ans = ['_'] * N

        ans[1] = word[0]
        for i in range(3, N, 2):
            if word[i - 1] >= ans[i - 2]:
                ans[i] = chr(ord('A') + (ord(word[i - 1]) - ord(ans[i - 2])))
            else:
                ans[i] = chr(ord('A') + (ord(word[i - 1]) + 26 - ord(ans[i - 2])))

        ans[N - 2] = word[N - 1]
        for i in range(N - 4, -1, -2):
            if word[i + 1] >= ans[i + 2]:
                ans[i] = chr(ord('A') + (ord(word[i + 1]) - ord(ans[i + 2])))
            else:
                ans[i] = chr(ord('A') + (ord(word[i + 1]) + 26 - ord(ans[i + 2])))

        print(f"Case #{t + 1}: {''.join(ans)}")
