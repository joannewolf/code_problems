# d1000000
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000876ff1/0000000000a46471

T = int(input())
for t in range(T):
    N = int(input())
    S = [int(x) for x in input().split()]
    S.sort()

    ans = 0
    flag = 1
    for num in S:
        if num >= flag:
            ans += 1
            flag += 1

    print(f"Case #{t + 1}: {ans}")
