# Double or One Thing
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000877ba5/0000000000aa8e9c

T = int(input())
for t in range(T):
    S = input()
    N = len(S)

    count = 1
    ans = ""
    for i in range(N - 1):
        if S[i] > S[i+1]:
            ans += S[i] * count
            count = 1
        elif S[i] < S[i+1]:
            ans += S[i] * (2 * count)
            count = 1
        else:
            count += 1
    ans += S[-1] * count

    print(f"Case #{t + 1}: {ans}")
