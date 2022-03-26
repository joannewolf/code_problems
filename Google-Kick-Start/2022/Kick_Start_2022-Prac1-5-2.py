# Milk Tea
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000008f4332/0000000000943934
# Same with 2018-E-2
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050ff5/0000000000051185
# Build up the best bits one bit at a time, and only need to maintain first M+1 options
# Key idea: S_k: the best M+1 options with first k bits, each bits in S_{k+1} must have prefix in S_k
# O(PN + PMlogM + M)

INT_MAX = pow(10, 5)

T = int(input())
for t in range(T):
    [N, M, P] = map(int, input().split())
    preferences = []
    for _ in range(N):
        preferences.append(input())
    forbidden = set()
    for _ in range(M):
        forbidden.add(input())

    bit0_count = [0] * P
    bit1_count = [0] * P
    for i in range(N):
        for j in range(P):
            if preferences[i][j] == '0':
                bit0_count[j] += 1
            else:
                bit1_count[j] += 1
    # print(bit0_count)
    # print(bit1_count)
    
    best_bits = [("", 0)]
    for p in range(P):
        next_best = []
        for (bits, num) in best_bits:
            next_best.append((bits + "0", num + bit1_count[p]))
            next_best.append((bits + "1", num + bit0_count[p]))
        next_best.sort(key=lambda x: x[1])
        if M < len(next_best):
            # Consider tie
            last_num = next_best[M][1]
            flag = M
            for i in range(M, len(next_best)):
                if next_best[i][1] == last_num:
                    flag += 1
                else:
                    break
            best_bits = next_best[0 : flag]
        else:
            best_bits = next_best

    ans = INT_MAX
    for (bits, num) in best_bits:
        if bits not in forbidden and num < ans:
            ans = num
    print(f"Case #{t + 1}: {ans}")
