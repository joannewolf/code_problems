# Broken Clock
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000435baf/00000000007ae694
# We don't know which clock hand is H/M/S, so we try all possible permutation = 3!
# Assume the final time is h * 3600 * 10^9 + n', n' = m * 60 * 10^9 + s * 10^9 + n
# H + X(rotation) = h * 3600 * 10^9 + n'
# M + X = 12 * n'                        -> H - M = h * 3600 * 10^9 - 11 * n'
# S + X = 720 * (s * 10^9 + n)
# Try all possible h(0 ~ 11) to see if we can get integer n', and validate using S

from itertools import permutations

ROUND_TICK = 12 * 3600 * pow(10, 9)

T = int(input())
for t in range(T):
    [A, B, C] = [int(n) for n in input().split()]

    for [H, M, S] in permutations([A, B, C]):
        done = False
        for h in range(0, 12):
            if (h * 3600 * pow(10, 9) - H + M) % 11 == 0:
                n = (h * 3600 * pow(10, 9) - H + M) // 11 # n'
                # print("h", h, "n", n, ((H - h * 3600 * pow(10, 9) - n) - (S - 720 * (n % (60 * pow(10, 9))))))
                # Check the rotation of S hand is the same
                if ((H - h * 3600 * pow(10, 9) - n) - (S - 720 * (n % (60 * pow(10, 9))))) % ROUND_TICK == 0:
                    # n' could be minus, m/s/n, could be minus or 60 / 10^9
                    h = (h + (n // (60 * pow(10, 9)) // 60) + 12) % 12
                    m = (n // (60 * pow(10, 9)) + 60) % 60
                    s = (n % (60 * pow(10, 9)) // pow(10, 9) + 60) % 60
                    n = (n % (60 * pow(10, 9)) % pow(10, 9) + pow(10, 9)) % pow(10, 9)
                    print(f"Case #{t + 1}: {h} {m} {s} {n}")
                    done = True
                    break
        if done:
            break
