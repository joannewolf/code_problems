# Dance Battle
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000201d29/0000000000201c02

T = int(input())
for t in range(T):
    [E, N] = [int(x) for x in input().split()]
    skills = [int(x) for x in input().split()]
    skills.sort()

    ans = 0
    flag_l = 0
    flag_r = N - 1
    while flag_l <= flag_r:
        # print("E", E, flag_l, flag_r)
        if skills[flag_l] < E:
            E -= skills[flag_l]
            flag_l += 1
            ans += 1
        elif ans == 0 or flag_l == flag_r:
            break
        else:
            E += skills[flag_r]
            flag_r -= 1
            ans -= 1

    print(f"Case #{t + 1}: {ans}")
