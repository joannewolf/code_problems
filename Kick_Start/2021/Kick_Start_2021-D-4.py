# Primes and Queries
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000004361e3/000000000082bcf4
# Lifting-the-exponent lemma https://en.wikipedia.org/wiki/Lifting-the-exponent_lemma
# V(a^n − b^n) = V(a − b) + V(n), in this problem, a = Ai, b = Ai mod P, n = S
# When P = 2 and n is even, V(a^n − b^n) = V(a − b) + V(a + b) + V(n) - 1
# Handle Ai in 2 cases:
# (1) When Ai / val divisible by P
#     V(Ai^S - (Ai mod P)^S) = V(Ai^S - 0) = S * V(Ai)
# (2) When Ai / val not divisible by P
#     V(Ai^S - (Ai mod P)^S) = V(Ai − (Ai mod P)) + V(S)
#     V(Ai^S - (Ai mod P)^S) = V(Ai − (Ai mod P)) + V(S) + V(Ai + (Ai mod P)) - 1, when P = 2 and S is even
# If using array for recording, O(Nlog(max(Ai)) + Q*O(max(log(val) + 1,                               log(S) + N)) = O(Nlog(max(Ai)) + Q*O(N + log(max(S, val))))
#                                  ^^^ for get_V(Ai)      ^^^ query type 1, get_V(val) and update arr ^^^ query type 2, get_val(S) and get sum
# If using segment tree for recording range sum, O(Nlog(max(Ai)) + Q*O(log(max(S, val))) + logN)

def get_V(P: int, num: int):
    if num == 0:
        return 0
    count = 0
    while num % P == 0:
        count += 1
        num /= P
    return count

T = int(input())
for t in range(T):
    [N, Q, P] = [int(n) for n in input().split()]
    A = [int(n) for n in input().split()]

    arr1 = [0] * N # record V(Ai) for Ai divisible by P
    arr2 = [0] * N # record V(Ai − (Ai mod P)) for Ai not divisible by P
    arr3 = [0] * N # record V(Ai + (Ai mod P)) - 1 for Ai not divisible by P
    arr4 = [0] * N # 1 when Ai not divisible by P
    for i in range(N):
        if A[i] < P:
            continue
        elif A[i] % P == 0:
            arr1[i] = get_V(P, A[i])
        else:
            arr2[i] = get_V(P, A[i] - (A[i] % P))
            arr3[i] = get_V(P, A[i] + (A[i] % P)) - 1
            arr4[i] = 1

    result = []
    for i in range(Q):
        temp = [int(n) for n in input().split()]
        if temp[0] == 1:
            [_, pos, val] = temp
            pos -= 1
            A[pos] = val
            if val < P:
                arr1[pos] = 0
                arr2[pos] = 0
                arr3[pos] = 0
                arr4[pos] = 0
            elif val % P == 0:
                arr1[pos] = get_V(P, val)
                arr2[pos] = 0
                arr3[pos] = 0
                arr4[pos] = 0
            else:
                arr1[pos] = 0
                arr2[pos] = get_V(P, val - (val % P))
                arr3[pos] = get_V(P, val + (val % P)) - 1
                arr4[pos] = 1
        else:
            [_, S, L, R] = temp
            V_S = get_V(P, S)
            temp_result = S * sum(arr1[L - 1: R]) + sum(arr2[L - 1: R]) + sum(arr4[L - 1: R]) * V_S
            if P == 2 and S % 2 == 0:
                temp_result += sum(arr3[L - 1: R])

            result.append(temp_result)

    print(f"Case #{t + 1}: {' '.join([str(n) for n in result])}")
