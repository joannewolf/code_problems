# K-Goodness String
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000436140/000000000068cca3

T = input()
for t in range(int(T)):
    [N, K] = [int(n) for n in input().split()]
    s = input()
    score = 0
    for i in range(0, N // 2):
        # print(s[i], s[-1-i])
        if (s[i] != s[-1-i]):
            score += 1

    print("Case #{}: {}".format(t + 1, abs(K - score)))
