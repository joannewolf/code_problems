# Cheating Detection
# https://codingcompetitions.withgoogle.com/codejam/round/000000000043580a/00000000006d1155
# Choose the person with max correct rate, pass test set 1

T = int(input())
P = int(input())
for t in range(T):
    max_rate = 0.0
    index = -1
    for i in range(100):
        S = input()
        score_sum = 0
        for s in S:
            score_sum += int(s)
        # print(i, score_sum / 10000)
        if (score_sum / 10000 > max_rate):
            max_rate = score_sum / 10000
            index = i + 1

    print("Case #{}: {}".format(t + 1, index))
