# Yogurt
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050ff5/00000000000510f1

T = int(input())
for t in range(T):
    [N, K] = [int(x) for x in input().split()]
    expire = [int(x) for x in input().split()]

    expire.sort()
    days = []
    for i in range(N // K + 1):
        days.extend([i] * K)

    ans = 0
    flag_e = 0
    flag_d = 0
    while flag_e < N:
        if expire[flag_e] > days[flag_d]:
            ans += 1
            flag_e += 1
            flag_d += 1
        else:
            flag_e += 1

    print(f"Case #{t + 1}: {ans}")
