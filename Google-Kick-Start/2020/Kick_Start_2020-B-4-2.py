# Wandering Robot
# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ffc8/00000000002d8565
# The only way to pass is to go bottom-left or upper-right path
# For example, if going bottom-left path, it has to pass one of the cell (L - 1, D + 1), (L - 2, D + 2), ...
# And after passing one of those cell, it will never fail, so ans is to sum up the prob of those cells
# For example, the prod of (L - 1, D + 1) is when n = L + D - 2, C(n, k) * 0.5^(n) = n! / k! / (n - k)! / 2^n
# The big number can be noted as log => e^(ln(n!) - ln(k!) - ln((n - k)!) - n * ln(2))
# Constant time to pre-calculate all ln(n!) and n * ln(2) for n: 2 ~ W+H
# Then there are at most O(max(W, H)) critical cell, so O(max(W, H))

import math

MAX_N = 200010
log_frac = [0]
log_2 = [0]
for i in range(1, MAX_N):
    # log_frac[i] = ln(i!) = ln(i) + ln(i - 1) + ...
    log_frac.append(log_frac[i-1] + math.log(i))
for i in range(1, MAX_N):
    # log_2[i] = i * ln(2)
    log_2.append(log_2[i-1] + math.log(2))

def prob(N, K):
    return math.exp(log_frac[N] - log_frac[K] - log_frac[N - K] - log_2[N])

T = int(input())
for t in range(T):
    [W, H, L, U, R, D] = [int(n) for n in input().split()]

    ans = 0
    # Upper right
    flag_x = R - 1
    flag_y = U - 1
    if R < W:
        mult = 1
        while flag_y > 0:
            flag_y -= 1
            flag_x += 1
            if flag_x >= W - 1:
                # The cell on last column can only come from up cell
                flag_x = W - 2
                mult = 0.5
            ans += mult * prob(flag_x + flag_y, flag_x)

    # Lower left
    flag_y = D - 1
    flag_x = L - 1
    if D < H:
        mult = 1
        while flag_x > 0:
            flag_x -= 1
            flag_y += 1
            if flag_y >= H - 1:
                # The cell on last row can only come from left cell
                flag_y = H - 2
                mult = 0.5
            ans += mult * prob(flag_x + flag_y, flag_x)

    print(f"Case #{t + 1}: {ans}")
