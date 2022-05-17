# Copy & Paste
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000201bfe/0000000000201c96

def solve(i: int, copy: str):
    # print("i", i, "copy", copy)
    if (i, copy) in dp:
        return dp[(i, copy)]
    if i == N:
        return 0

    # Option 1: directly add next char
    res = 1 + solve(i + 1, copy)
    # Option 2: directly paste the clipboard str
    if copy != "" and copy == S[i : i + len(copy)]:
        res = min(res, 1 + solve(i + len(copy), copy))
    # Option 3: copy then paste
    for j in range(i+1, N+1):
        if S[i:j] in S[0:i]:
            next_copy = S[i:j]
            # print("i", i, "j", j, next_copy)
            res = min(res, 2 + solve(j, next_copy))
        else:
            break

    dp[(i, copy)] = res
    return res

T = int(input())
for t in range(T):
    S = input()
    N = len(S)
    dp = {}

    ans = solve(0, "")
    print(f"Case #{t + 1}: {ans}")
