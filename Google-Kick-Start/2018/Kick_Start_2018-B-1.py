# No Nine
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050ff4/0000000000051183
# To calculate the # of legal numbers from [0, X]
# Let x0, x1, ... x_{n-1} be the decimal representation of X, i.e. X = SUM{x_i * 10^i}, 0 <= i < n
# When 1 <= i < n, take one digit at a time, under xi * 10^i, if we construct number without using 9, there will be xi * 9^i numbers
# For example, X = 7463, x3 = 7, means for numbers < 7000, there are 7 (0 ~ 6) * 9^3 (0 ~ 8) possible numbers without using 9
#   for numbers 7000 <= 7463, check next digit x2 = 4, and so on, eventually we get C = SUM{x_i * 9^i}, 1 <= i < n
# C is divisible by 9, for all numbers in C, it must be in form {10*X + 0, 10*X + 1, ..., 10*X + 8}, cuz we don't use 9 in one's digit
# And there must be one number out of it is divisible by 9, so the # of legal numbers = C * 8 / 9
# For the rest [X - x0, X], we just check one by one

def count(num: str):
    n = len(num)
    temp = 0
    base = 9
    for i in range(n - 2, -1, -1):
        temp += int(num[i]) * base
        base *= 9

    ans = temp * 8 // 9
    for i in range(int(num) - int(num[-1]), int(num) + 1):
        if '9' not in str(i) and i % 9 != 0:
            ans += 1

    # print(num, ans)
    return ans

T = int(input())
for t in range(T):
    [F, L] = input().split()

    print(f"Case #{t + 1}: {count(L) - count(F) + 1}")
