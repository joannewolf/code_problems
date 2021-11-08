# Longest Arithmetic
# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff47/00000000003bf4ed

T = int(input())
for t in range(T):
    N = int(input())
    num = [int(n) for n in input().split()]

    ans = 0
    count = 2
    diff = num[1] - num[0]
    for i in range(2, N):
        if num[i] - num[i - 1] == diff:
            count += 1
        else:
            ans = max(ans, count)
            count = 2
            diff = num[i] - num[i - 1]
    ans = max(ans, count)

    print(f"Case #{t + 1}: {ans}")
