# Hacked Exam
# https://codingcompetitions.withgoogle.com/codejam/round/000000000043585d/0000000000754750
# Define p_q as the probability that the answer of question q is T
# Expected score = sum(p_q) for questions we answer T + sum(1 - p_q) for questions we answer F
# If p_q > 1/2, we choose to answer T; if p_q < 1/2, we choose to answer F; if p_q == 1/2, it doesn't matters
# If multiple questions get same answers from all the students, they have same p

import math

comb = []
comb.append([1])
for i in range(1, 121): # Since there's at most 120 questions
    temp = [1]
    for j in range(1, i):
        temp.append(comb[i-1][j-1] + comb[i-1][j])
    temp.append(1)
    comb.append(temp)

T = int(input())
for t in range(T):
    [N, Q] = [int(n) for n in input().split()]
    answer = []
    score = []
    for i in range(N):
        [A, S] = input().split()
        answer.append(A)
        score.append(int(S))

    if (N == 1):
        if (score[0] >= Q / 2):
            print("Case #{}: {} {}/1".format(t + 1, answer[0], score[0]))
        else:
            ans = ""
            for a in answer[0]:
                ans += ('F' if a == 'T' else 'T')
            print("Case #{}: {} {}/1".format(t + 1, ans, Q - score[0]))
    elif (N == 2):
        # When N == 2, there's only 4 types of questions p_TT, p_FF, p_TF, p_FT, and p_TT = 1 - p_FF, p_TF = 1 - p_FT
        # We can represent the expected score of both students' answer with equation of p_TT and p_TF, and get two unknowns
        # For 4 types of questions, p_TT, p_FF, p_TF, p_FT, we choose T if p_q > 1/2 and choose F vice versa
        # Based on whether p_TT, p_FF, p_TF, p_FT is > or < 1/2, we have 4 answering strategy
        # If (p_TT > 1/2 -> choose T, p_FF < 1/2 -> choose F), (p_TF > 1/2 -> choose T, p_FT < 1/2 -> choose F) --> choose first student's answer
        # If (p_TT > 1/2 -> choose T, p_FF < 1/2 -> choose F), (p_TF < 1/2 -> choose F, p_FT > 1/2 -> choose T) --> choose second student's answer
        # If (p_TT < 1/2 -> choose F, p_FF > 1/2 -> choose T), (p_TF > 1/2 -> choose T, p_FT < 1/2 -> choose F) --> choose second student's opposite answer
        # If (p_TT < 1/2 -> choose F, p_FF > 1/2 -> choose T), (p_TF < 1/2 -> choose F, p_FT > 1/2 -> choose T) --> choose first student's opposite answer
        # Reversely, from 4 possible choices, we compare S1, S2, Q - S1, Q - S2 and choose the max one
        max_score = max(score[0], score[1], Q - score[0], Q - score[1])
        if (score[0] == max_score):
            max_answer = answer[0]
        elif (score[1] == max_score):
            max_answer = answer[1]
        elif (Q - score[0] == max_score):
            max_answer = ""
            for a in answer[0]:
                max_answer += ('F' if a == 'T' else 'T')
        elif (Q - score[1] == max_score):
            max_answer = ""
            for a in answer[1]:
                max_answer += ('F' if a == 'T' else 'T')

        print("Case #{}: {} {}/1".format(t + 1, max_answer, max_score))
    elif (N == 3):
        # When N == 3, there's p_TTT = 1 - p_FFF, p_TTF = 1 - p_FFT, p_TFT = 1 - p_FTF, p_FTT = 1 - p_TFF, we have 3 equation to solve 4 unknowns
        # Catagarize questions into 4 types (TTT or FFF), (TTF or FFT), (TFT or FTF), (FTT or TFF)
        ABC = 0
        AB = 0
        AC = 0
        BC = 0
        for i in range(Q):
            if (answer[0][i] == answer[1][i] and answer[0][i] == answer[2][i]):
                ABC += 1
            elif (answer[0][i] == answer[1][i] and answer[0][i] != answer[2][i]):
                AB += 1
            elif (answer[0][i] != answer[1][i] and answer[0][i] == answer[2][i]):
                AC += 1
            elif (answer[0][i] != answer[1][i] and answer[0][i] != answer[2][i]):
                BC += 1

        total = 0
        score_ABC = 0
        score_AB = 0
        score_AC = 0
        score_BC = 0
        # For each type, assume we answer abc, ab, ac, bc questions correctly following majority's answer, how many tuples (abc, ab, ac, bc) match 3 student's score?
        for ab in range(AB + 1):
            for ac in range(AC + 1):
                for bc in range(BC + 1):
                    temp_abc = score[0] - (ab + ac + (BC - bc)) # For student A, they didn't answer majority's answer for BC type, so they get (BC - bc) score for that type
                    if (temp_abc < 0 or temp_abc > ABC):
                        continue
                    if (score[1] != ab + (AC - ac) + bc + temp_abc):
                        continue
                    if (score[2] != (AB - ab) + ac + bc + temp_abc):
                        continue
                    # Get a match tuple of (abc, ab, ac, bc), for this tuple, how many combinations of answer does it have?
                    # num_comb = math.comb(ABC, temp_abc) * math.comb(AB, ab) * math.comb(AC, ac) * math.comb(BC, bc)
                    num_comb = comb[ABC][temp_abc] * comb[AB][ab] * comb[AC][ac] * comb[BC][bc]
                    total += num_comb
                    # And what's the expected score if we follow majority's answer?
                    score_ABC += num_comb * temp_abc
                    score_AB += num_comb * ab
                    score_AC += num_comb * ac
                    score_BC += num_comb * bc
        
        # For 4 types of questions, choose whether to follow majority
        ans = ""
        best_score = 0
        follow_maj_ABC = (score_ABC > ABC * total - score_ABC)
        best_score += score_ABC if follow_maj_ABC else (ABC * total - score_ABC)
        follow_maj_AB = (score_AB > AB * total - score_AB)
        best_score += score_AB if follow_maj_AB else (AB * total - score_AB)
        follow_maj_AC = (score_AC > AC * total - score_AC)
        best_score += score_AC if follow_maj_AC else (AC * total - score_AC)
        follow_maj_BC = (score_BC > BC * total - score_BC)
        best_score += score_BC if follow_maj_BC else (BC * total - score_BC)

        for i in range(Q):
            if (answer[0][i] == answer[1][i] and answer[0][i] == answer[2][i]):
                ans += answer[0][i] if follow_maj_ABC else ('T' if answer[0][i] == 'F' else 'F')
            elif (answer[0][i] == answer[1][i] and answer[0][i] != answer[2][i]):
                ans += answer[0][i] if follow_maj_AB else answer[2][i]
            elif (answer[0][i] != answer[1][i] and answer[0][i] == answer[2][i]):
                ans += answer[0][i] if follow_maj_AC else answer[1][i]
            elif (answer[0][i] != answer[1][i] and answer[0][i] != answer[2][i]):
                ans += answer[1][i] if follow_maj_BC else answer[0][i]

        gcd = math.gcd(best_score, total)
        best_score //= gcd
        total //= gcd
        print("Case #{}: {} {}/{}".format(t + 1, ans, best_score, total))
