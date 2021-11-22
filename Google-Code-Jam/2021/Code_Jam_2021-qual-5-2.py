# Cheating Detection
# https://codingcompetitions.withgoogle.com/codejam/round/000000000043580a/00000000006d1155
# Assume the cheater has base skill level B, and becomes skill level B + Δ
# However this cheater does worse on easy problem than a player with real B + Δ skill level, and better on hard problem
# From ksun48's answer, explanation https://www.youtube.com/watch?v=7RM9GNOsjJY

T = int(input())
P = int(input())
NUM_PLAYER = 100
NUM_PROBLEM = 10000
for t in range(T):
    matrix = []
    # Number of correct answer for each player
    p_solved = [0] * NUM_PLAYER
    # Number of person answer the problem correct for each problem
    q_solved = [0] * NUM_PROBLEM
    for i in range(NUM_PLAYER):
        matrix.append(input())
        for j in range(NUM_PROBLEM):
            if (matrix[i][j] == '1'):
                p_solved[i] += 1
                q_solved[j] += 1

    # Sort problem index based on correctness rate high to low (easy to hard)
    q_index = list(range(0, NUM_PROBLEM))
    q_index.sort(key=lambda i: q_solved[i], reverse=True)
    # for i in range(NUM_PROBLEM):
    #     print(i, q_index[i], q_solved[q_index[i]])

    score = [0] * NUM_PLAYER
    for i in range(NUM_PLAYER):
        flag0 = 0
        inv = 0
        for j in range(NUM_PROBLEM):
            if (matrix[i][q_index[j]] == '1'):
                # flag0 means the # of incorrect answers easier than current correct answer
                inv += flag0
            else:
                flag0 += 1
        # Divide by (1 - p_solved[i]) for getting the percentage of [# of incorrect answers easier than current correct answer] out of all incorrect answers
        # Divide by p_solved[i] for getting weighted average
        score[i] = inv / (NUM_PROBLEM - p_solved[i]) / p_solved[i]

    print("Case #{}: {}".format(t + 1, score.index(max(score)) + 1))
