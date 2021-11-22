# Interleaved Output: Part 2
# https://codingcompetitions.withgoogle.com/codejamio/round/000000000019ff03/00000000001b5cd7
# DP, O(N*2^4)

T = raw_input()
for t in xrange(int(T)):
    S = raw_input()

    # dp[j][i]: the max number of IOs in string S[:i] and 4 machine (IO, Io, iO, io) in state j
    # state j: j in bits b1b2b3b4, IO is printing b1-th character (0-th -> I, 1-th -> O), similar for Io, iO, io machine
    dp = [[-1 for i in range(len(S))] for j in range(16)]
    if S[0] == 'I':
        dp[1][0] = 0
        dp[2][0] = 0
    if S[0] == 'i':
        dp[4][0] = 0
        dp[8][0] = 0

    for i in range(1, len(S)):
        c = S[i]
        if c == 'I':
            # IO bit 0 -> 1 or Io bit 0 -> 1
            for j in range(16):
                if j & 1 != 0 and dp[j - 1][i - 1] != -1:
                    dp[j][i] = max(dp[j][i], dp[j - 1][i - 1])
                if j & 2 != 0 and dp[j - 2][i - 1] != -1:
                    dp[j][i] = max(dp[j][i], dp[j - 2][i - 1])
        elif c == 'i':
            # iO bit 0 -> 1 or io bit 0 -> 1
            for j in range(16):
                if j & 4 != 0 and dp[j - 4][i - 1] != -1:
                    dp[j][i] = max(dp[j][i], dp[j - 4][i - 1])
                if j & 8 != 0 and dp[j - 8][i - 1] != -1:
                    dp[j][i] = max(dp[j][i], dp[j - 8][i - 1])
        elif c == 'O':
            # IO bit 1 -> 0 or iO bit 1 -> 0
            for j in range(16):
                if j & 1 == 0 and dp[j + 1][i - 1] != -1:
                    dp[j][i] = max(dp[j][i], dp[j + 1][i - 1] + 1)
                if j & 4 == 0 and dp[j + 4][i - 1] != -1:
                    dp[j][i] = max(dp[j][i], dp[j + 4][i - 1])
        elif c == 'o':
            # Io bit 1 -> 0 or io bit 1 -> 0
            for j in range(16):
                if j & 2 == 0 and dp[j + 2][i - 1] != -1:
                    dp[j][i] = max(dp[j][i], dp[j + 2][i - 1])
                if j & 8 == 0 and dp[j + 8][i - 1] != -1:
                    dp[j][i] = max(dp[j][i], dp[j + 8][i - 1])

    print "Case #{}: {}".format(t + 1, dp[0][-1])