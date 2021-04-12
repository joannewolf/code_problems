import math

# Pre-calculate C(n, m)

MAXN = 128
comb = [None] * MAXN
comb[0] = [1]
for i in range(1, MAXN):
    comb[i] = [1]
    for j in range(1, i):
        comb[i].append(comb[i-1][j-1] + comb[i-1][j])
    comb[i].append(1)
# print(comb)

T = int(input())

for t in range(1, T+1):
    N, Q = map(int, input().split())
    S = [0] * (N+1)
    A = [""] * (N+1)

    for i in range(1, N+1):
        A[i], S[i] = input().split()
        S[i] = int(S[i])

    # Calculate most common answer
    a0 = []
    for i in range(Q):
        t_cnt = sum(A[j][i] == 'T' for j in range(1, N+1))
        a0.append('T' if t_cnt >= (N - t_cnt) else 'F')
    A[0] = ''.join(a0)

    print(N, Q, A, S)

    diff_set = [None] * (N+1)
    
    # Calculate diff sets
    for i in range(1, N+1):
        diff_set[i] = set()
        for j in range(Q):
            if A[i][j] != A[0][j]:
                diff_set[i].add(j)
    n = [0] * (N+1)
    # n[0] = Q - sum(n[1:])
    diff_set[0] = set(range(Q)).difference(set().union(*diff_set[1:])) # The questions with all T of F
    for i in range(N+1):
        n[i] = len(diff_set[i])

    print(diff_set)
    print(n)

    # Calculate number of sequences
    num_true = [0] * Q
    num_total = 0

    for s0 in range(0, Q+1): # enumerate num of corrects of default answer
        ok = True
        alpha = [0] * (N+1)
        beta = [0] * (N+1)
        alpha[0] = s0
        for i in range(1, N+1):
            d = S[i] - s0
            if (d + n[i]) % 2 != 0:
                ok = False
                break
            alpha[i] = (n[i] + d) // 2
            beta[i] = (n[i] - d) // 2
            alpha[0] -= beta[i]
            if alpha[i] < 0 or beta[i] < 0:
                ok = False
                break
        beta[0] = n[0] - alpha[0]
        if alpha[0] < 0 or beta[0] < 0:
            ok = False
        if not ok:
            continue
        

        num_seq = 1
        for i in range(N+1):
            num_seq *= comb[n[i]][alpha[i]]
        num_total += num_seq

        print(f"S0 = {s0}, Alpha = {alpha}, Beta = {beta}, #Seq = {num_seq}")

        # Calc true nums

        for i in range(0, N+1):
            if n[i] == 0:
                continue
            nt = (num_seq * alpha[i]) // n[i]
            if i >= 1:
                nt = num_seq - nt
            for idx in diff_set[i]:
                nt_idx = nt
                if A[0][idx] == 'F':
                    nt_idx = num_seq - nt_idx
                num_true[idx] += nt_idx

    # print("Total nseq", num_total)

    ans_string = []
    best_nominator = 0
    for i in range(Q):
        if num_true[i] > num_total - num_true[i]:
            ans_string.append('T')
            best_nominator += num_true[i]
        else:
            ans_string.append('F')
            best_nominator += num_total - num_true[i]
    ans_string = ''.join(ans_string)

    # print(ans_string)
    # print(best_nominator // 344100)

    gcd = math.gcd(best_nominator, num_total)
    nominator = best_nominator // gcd
    denominator = num_total // gcd
    print(f'Case #{t}: {ans_string} {nominator}/{denominator}')

