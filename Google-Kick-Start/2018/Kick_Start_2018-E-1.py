# Board Game
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050ff5/0000000000051184
# Brute-force, 9!/3!/3!/3!=1680, O(1680^2), TLE but correct locally on test set 2

three_battle = []

# Enumerate all possible card distribution
# e.g. [0, 0, 0, 1, 1, 1, 2, 2, 2] mean first three cards in first battlefield, middle three cards in second battlefield, and the rest in third battlefield
def gen_battle(now, count):
    if len(now) == 9:
        three_battle.append(now)
    else:
        for i in range(3):
            if count[i] > 0:
                count[i] -= 1
                gen_battle(now + [i], count)
                count[i] += 1

def battle(A: list, B: list):
    win = 0
    for i in range(3):
        if A[i] > B[i]:
            win += 1
    return (win > 1)

T = int(input())
gen_battle([], [3, 3, 3])
for t in range(T):
    N = int(input())
    A = [int(x) for x in input().split()]
    B = [int(x) for x in input().split()]

    score_A = []
    score_B = []
    for choice_A in three_battle:
        temp_score = [0] * 3
        for i in range(9):
            temp_score[choice_A[i]] += A[i]
        score_A.append(temp_score)
    for choice_B in three_battle:
        temp_score = [0] * 3
        for i in range(9):
            temp_score[choice_B[i]] += B[i]
        score_B.append(temp_score)

    ans = 0
    for score_a in score_A:
        count = 0
        win = 0
        for score_b in score_B:
            count += 1
            if battle(score_a, score_b):
                win += 1
        if win / count > ans:
            ans = win / count

    print(f"Case #{t + 1}: {ans}")

