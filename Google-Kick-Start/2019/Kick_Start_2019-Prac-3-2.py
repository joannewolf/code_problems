# Kickstart Alarm
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000051060/0000000000058a56
# Same with 2018-C-3
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050ee0/0000000000051133
# subarray len
# 1       2               3           ...     N
# A1      A1,A2           A1,A2,A3            A1,A2,...,A{N}
# A2      A2,A3           A2,A3,A4
# ...
# A{N-2}  A{N-2},A{N-1}   A{N-2},A{N-1},A{N}
# A{N-1}  A{N-1},A{N}
# A{N}
# 1^i     1^i,2^i         1^i,2^i,3^i         1^i,2^i,...,N^i

# subarray len
# 1           2                   3                   ... N-1                         N
# A1*1^i      A1*1^i              A1*1^i                  A1*1^i                      A1*1^i
# A2*1^i      A2*(1^i+2^i)        A2*(1^i+2^i)            A2*(1^i+2^i)                A2*2^i
# A3*1^i      A3*(1^i+2^i)        A3*(1^i+2^i+3^i)        A3*(2^i+3^i)                A3*3^i
# ...
# A{N-2}*1^i  A{N-2}*(1^i+2^i)    A{N-2}*(1^i+2^i+3^i)    A{N-2}*((N-3)^i+(N-2)^i)    A{N-2}*(N-2)^i
# A{N-1}*1^i  A{N-1}*(1^i+2^i)    A{N-1}*(2^i+3^i)        A{N-1}*((N-2)^i+(N-1)^i)    A{N-1}*(N-1)^i
# A{N}*1^i    A{N}*(2^i)          A{N}*(3^i)              A{N}*(N-1)^i                A{N}*N^i

# = A1*(N*1^i)
# = A2*((N-1)*1^i + (N-1)*2^i)
# = A3*((N-2)*1^i + (N-2)*2^i + (N-2)*3^i))
# ...
# = A{N-2}*(3*1^i + 3*2^i + ... + 3*(N-2)^i)
# = A{N-1}*(2*1^i + 2*2^i + ... + 2*(N-1)^i)
# = A{N}*(1^i + 2^i + ... + N^i)
# ==> i = 1...K, j = 1...N, SUM{Aj * (N - j + 1) * (1^i + ... + j^i)}
# ===> j = 1...N, SUM{j(j^K-1)/(j-1)) * (Aj*(N-j+1) + ... + A{N}*1)}
# or
# ===> j = 1...N, SUM{Aj * (N - j + 1) * (1*K + 2(2^K-1)/(2-1) + ... + j(j^K-1)/(j-1))}
# O(N*logK), logK for pow()

MOD = pow(10, 9) + 7

T = int(input())
for t in range(T):
    [N, K, x0, y0, C, D, Ex, Ey, F] = [int(n) for n in input().split()]
    A = [(x0 + y0) % F]
    for i in range(1, N):
        A.append((A[-1] * (C + D) + Ex + Ey) % F)
    # print(A)

    # Sum option 1
    # prefix_sum = [0] # prefix_sum[i] = SUM{Aj * (N - j)} for j = 1...i
    # for i in range(N):
    #     prefix_sum.append(prefix_sum[-1] + A[i] * (N-i))
    # ans = 0
    # for i in range(1, N + 1):
    #     if i == 1:
    #         ans += (prefix_sum[N] - prefix_sum[0]) * K % MOD
    #     else:
    #         ans += (prefix_sum[N] - prefix_sum[i-1]) * (i*(pow(i, K)-1)//(i-1))
    #     ans %= MOD

    # Sum option 2
    ans = 0
    sum = K
    for i in range(1, N + 1):
        if i != 1:
            sum += i*(pow(i, K)-1)//(i-1) % MOD
        sum %= MOD
        ans += A[i - 1] * (N - i + 1) * sum % MOD
        ans %= MOD

    print(f"Case #{t + 1}: {ans}")
