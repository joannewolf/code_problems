# Irregular Expressions
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000008f4a94/0000000000b55464

vowels = 'aeiou'

def has_vowel(S):
    res = False
    for v in vowels:
        res |= (v in S)
    return res

T = int(input())
for t in range(T):
    S = input()
    N = len(S)

    ans = False
    index = []
    for i in range(N):
        if S[i] in vowels:
            index.append((i, S[i]))
    # print(index)

    for i in range(len(index) - 3):
        for j in range(i + 2, len(index) - 1):
            if (index[i][1] == index[j][1] and
                index[i+1][1] == index[j+1][1] and
                index[i+1][0] - index[i][0] == index[j+1][0] - index[j][0] and
                S[index[i][0] : index[i+1][0]+1] == S[index[j][0] : index[j+1][0]+1] and
                has_vowel(S[index[i+1][0]+1 : index[j][0]])):
                # print(i, j, S[index[i+1][0]+1 : index[j][0]])
                ans = True
                break
        if ans:
            break

    if ans:
        print(f"Case #{t + 1}: Spell!")
    else:
        print(f"Case #{t + 1}: Nothing.")
