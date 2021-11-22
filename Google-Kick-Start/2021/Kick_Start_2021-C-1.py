# Smaller Strings
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435c44/00000000007ebe5e
# NOTE: The string S consists of lowercase letters from the first K letters of the English alphabet.

MOD = pow(10, 9) + 7

T = int(input())
for t in range(T):
    [N, K] = [int(n) for n in input().split()]
    S = input()

    # Every combination < S's first half
    result = 0
    for i in range(0, (N + 1) // 2):
        result = (result * K + ord(S[i]) - ord('a')) % MOD

    # For the combination == S's first half, check if second half < S
    for i in range(N // 2 - 1, -1, -1):
        if S[i] < S[N - i - 1]:
            result += 1
            break
        elif S[i] > S[N - i - 1]:
            break

    print(f"Case #{t + 1}: {result % MOD}")
