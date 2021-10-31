# Locked Doors
# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff08/0000000000386d5c
# O(N^2), MLE on test set 2
# If not memorize order, but compute the ans for each query, O(Q*N), TLE on test set 2

T = int(input())
for t in range(T):
    [N, Q] = [int(n) for n in input().split()]
    lock = [pow(10, 6)] + [int(n) for n in input().split()] + [pow(10, 6)]
    # lock[i] is between door i and door i + 1
    
    order = [[] for i in range(N + 1)]
    ans = []
    for i in range(Q):
        [S, K] = [int(n) for n in input().split()]
        if not order[S]:
            temp_order = [S]
            flag_left = S - 1
            flag_right = S
            while flag_left != 0 or flag_right != N:
                if lock[flag_left] < lock[flag_right]:
                    temp_order.append(flag_left)
                    flag_left -= 1
                else:
                    temp_order.append(flag_right + 1)
                    flag_right += 1
            order[S] = temp_order
            # print(S, order[S])
            ans.append(order[S][K - 1])
        else:
            ans.append(order[S][K - 1])

    print(f"Case #{t + 1}: {' '.join([str(n) for n in ans])}")
