# Palindrome Free Strings
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000008cb33e/00000000009e762e
# Brute-force, O(2^N * N), TLE on test set 2

def check(S: list):
    # print(S)
    first_unknown = -1
    for i in range(N):
        if S[i] == '?' and first_unknown == -1:
            first_unknown = i
        elif (i < N - 4 and S[i] != '?' and S[i] == S[i + 4]
            and S[i + 1] != '?' and S[i + 1] == S[i + 3]):
            return False
        elif (i < N - 5 and S[i] != '?' and S[i] == S[i + 5]
            and S[i + 1] != '?' and S[i + 1] == S[i + 4]
            and S[i + 2] != '?' and S[i + 2] == S[i + 3]):
            return False
    # print("first_unknown", first_unknown)
    if first_unknown != -1:
        res = False
        if not res:
            S1 = S.copy()
            S1[first_unknown] = '0'
            res |= check(S1)
        if not res:
            S2 = S.copy()
            S2[first_unknown] = '1'
            res |= check(S2)
        return res
    else:
        return True

T = int(input())
for t in range(T):
    N = int(input())
    S = list(input())

    ans = check(S)
    if ans:
        print(f"Case #{t + 1}: POSSIBLE")
    else:
        print(f"Case #{t + 1}: IMPOSSIBLE")
