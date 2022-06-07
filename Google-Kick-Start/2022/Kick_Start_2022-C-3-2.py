# Ants on a Stick
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000008cb4d1/0000000000b209bc
# Ants bouncing off -> all ants will maintain same relative position, only the leftmost or rightmost will drop in order
# List all drop-off events and print the ID
# O(NlogN)

T = int(input())
for t in range(T):
    [N, L] = [int(x) for x in input().split()]
    ants = []
    drop_time = []
    for i in range(N):
        [p, d] = [int(x) for x in input().split()]
        ants.append((i+1, p, d))
        if d == 0:
            drop_time.append((p, d))
        else:
            drop_time.append((L - p, d))
    ants.sort(key=lambda x: x[1]) # Sort by initial position
    drop_time.sort()
    # print(ants)
    # print(drop_time)

    ans = []
    flag_l, flag_r = 0, N-1
    drop_flag = 0
    while drop_flag < N:
        # If two ants fall off at the same time, print the smaller first
        if drop_flag < N - 1 and drop_time[drop_flag][0] == drop_time[drop_flag+1][0]:
            if ants[flag_l][0] < ants[flag_r][0]:
                ans.append(ants[flag_l][0])
                ans.append(ants[flag_r][0])
            else:
                ans.append(ants[flag_r][0])
                ans.append(ants[flag_l][0])
            flag_l += 1
            flag_r -= 1
            drop_flag += 2
        else:
            if drop_time[drop_flag][1] == 0:
                ans.append(ants[flag_l][0])
                flag_l += 1
            else:
                ans.append(ants[flag_r][0])
                flag_r -= 1
            drop_flag += 1


    print(f"Case #{t + 1}: {' '.join(map(str, ans))}")
