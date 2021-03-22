# Foregone Solution
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000051705/0000000000088231

T = input()
for t in range(int(T)):
    N = int(input())
    a = 0
    b = 0
    power = 1
    while (N != 0):
        # print(N, N % 10)
        if (N % 10 != 0 and N % 10 != 5):
            a += 1 * power
            b += (N % 10 - 1) * power
        elif (N % 10 == 5):
            a += 2 * power
            b += 3 * power
        N //= 10
        power *= 10
    print("Case #{}: {} {}".format(t + 1, a, b))
