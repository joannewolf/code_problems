# High Buildings
# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff47/00000000003bef73

T = int(input())
for t in range(T):
    [N, A, B, C] = [int(n) for n in input().split()]

    if A < C or B < C or A + B - C > N or (A == C and B == C and C == 1 and N > 1):
        print(f"Case #{t + 1}: IMPOSSIBLE")
        continue

    ans = [N - 1] * (A - C) + [N] * (C) + [N - 1] * (B - C)
    if C != 1 or B != C:
        ans = ans[:A - C + 1] + [1] * (N - (A + B - C)) + ans[A - C + 1:]
    else:
        ans = ans[:A - C] + [1] * (N - (A + B - C)) + ans[A - C:]

    print(f"Case #{t + 1}: {' '.join([str(n) for n in ans])}")
