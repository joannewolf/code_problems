# Magical Thinking v2
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000201c98/0000000000201c00

T = int(input())
for t in range(T):
    [N, Q] = [int(x) for x in input().split()]
    answers = []
    for _ in range(N+1):
        answers.append(input())
    scores = [int(x) for x in input().split()]

    # Greedy for N = 1
    if N == 1:
        same = 0
        diff = 0
        for i in range(Q):
            if answers[0][i] == answers[1][i]:
                same += 1
            else:
                diff += 1

        if scores[0] <= same:
            ans = scores[0] + diff
        else:
            ans = same + diff - (scores[0] - same)
        print(f"Case #{t + 1}: {ans}")

    elif N == 2:
        A = 0 # All same answer
        B = 0 # Same with first friend
        C = 0 # Same with second friend
        D = 0 # First and second friends are same but different with me
        for i in range(Q):
            if answers[0][i] == answers[1][i] and answers[1][i] == answers[2][i]:
                A += 1
            elif answers[0][i] != answers[1][i] and answers[0][i] == answers[2][i]:
                B += 1
            elif answers[0][i] != answers[1][i] and answers[1][i] == answers[2][i]:
                C += 1
            elif answers[0][i] == answers[1][i] and answers[0][i] != answers[2][i]:
                D += 1

        ans = 0
        for a in range(A+1):
            for b in range(B+1):
                for c in range(C+1):
                    for d in range(D+1):
                        if a + b + c + d == scores[0] and a + (B - b) + (C - c) + d == scores[1]:
                            ans = max(ans, a + b + (C - c) + (D - d))

        print(f"Case #{t + 1}: {ans}")
