# Speed Typing
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000008cb33e/00000000009e7021

T = int(input())
for t in range(T):
    I = input()
    P = input()
    NI = len(I)
    NP = len(P)

    flag_i = 0
    flag_p = 0
    while flag_i < NI and flag_p < NP:
        if I[flag_i] == P[flag_p]:
            flag_i += 1
            flag_p += 1
        else:
            flag_p += 1

    if flag_i == NI:
        print(f"Case #{t + 1}: {NP-NI}")
    else:
        print(f"Case #{t + 1}: IMPOSSIBLE")
