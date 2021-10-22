# Dogs and Cats
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000004362d6/00000000008b3771

T = int(input())
for t in range(T):
    [N, D, C, M] = [int(n) for n in input().split()]
    S = input()

    result = 0
    stop = N
    for i in range(N):
        if S[i] == 'D':
            if D > 0:
                D -= 1
                C += M
            else:
                stop = i
                break
        elif S[i] == 'C':
            if C > 0:
                C -= 1
            else:
                stop = i
                break

    if 'D' not in S[stop:]:
        print(f"Case #{t + 1}: YES")
    else:
        print(f"Case #{t + 1}: NO")
