# Huge Numbers
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000201b7d/0000000000201c03
# A^(N!) = (((A^1)^2)^3)...^N
# O(NlogN)

T = int(input())
for t in range(T):
    [A, N, P] = [int(x) for x in input().split()]

    ans = A % P
    for i in range(2, N+1):
        num = i
        next_ans = 1
        while num != 0:
            if num & 1:
                next_ans = next_ans * ans % P
            num //= 2
            ans = ans * ans % P
        ans = next_ans

    print(f"Case #{t + 1}: {ans}")
