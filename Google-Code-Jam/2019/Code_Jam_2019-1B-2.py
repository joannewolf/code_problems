# Draupnir
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000051706/0000000000122837
# In day n, total coin = 2^(n/1)*R1 + 2^(n/2)*R2 + 2^(n/3)*R3 + 2^(n/4)*R4 + 2^(n/5)*R5 + 2^(n/6)*R6
# 0 <= Ri <= 100 ~= 2^6.... -> as long as 2^(n/(i+1)) - 2^(n/i) >= 7, I can confirm the R(i+1), cuz even if Ri = 100, it will not confuse the number of 2^(n/(i+1))
# When choosing n, be careful not let any num > 2^63 and % 2^63 != 0, e.g. 2^60*4 % 2^63 == 2^60*100 % 2^63, cannot tell if R is 4 or 100

import sys

[T, W] = [int(n) for n in input().split()]
for t in range(int(T)):
    print("56")
    sys.stdout.flush()
    n56 = int(input())
    # n56 = 2^56*R1 + 2^28*R2 + 2^18*R3 + 2^14*R4 + 2^11*R5 + 2^9*R6
    print("150")
    sys.stdout.flush()
    n150 = int(input())
    # n150 = 2^150*R1 + 2^75*R2 + 2^50*R3 + 2^37*R4 + 2^30*R5 + 2^25*R6

    result = [0] * 6

    result[0] = n56 // pow(2, 56)
    n56 -= result[0] * pow(2, 56)

    result[1] = n56 // pow(2, 28)
    n56 -= result[1] * pow(2, 28)

    result[2] = n150 // pow(2, 50)
    n150 -= result[2] * pow(2, 50)
    n56 -= result[2] * pow(2, 18)

    result[3] = n150 // pow(2, 37)
    n150 -= result[3] * pow(2, 37)
    n56 -= result[3] * pow(2, 14)

    # Eventually we can solve binary linear equation to get R5, R6
    # n56' = 2^11*R5 + 2^9*R6   ->  n56'/2^9 = 4*R5 + R6    ->  R5 = (n150'/2^25 - n56'/2^9) / 28
    # n150' = 2^30*R5 + 2^25*R6     n150'/2^25 = 32*R5 + R6
    result[4] = (n150 // pow(2, 25) - n56 // pow(2, 9)) // 28
    result[5] = n56 // pow(2, 9) - 4 * result[4]

    print(' '.join([str(i) for i in result]))
    sys.stdout.flush()
    ans = int(input())
    if (ans == 1):
        continue
    elif (ans == -1):
        sys.exit(1)
