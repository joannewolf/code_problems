# Interesting Integers
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000008cb33e/00000000009e73ea
# Top-down DP with memorization
# Let M = len(B), O(for l = 1...M sum{((l+9-1)! / ((9-1)!l!) + 1) * 9l})

dp = {}
# dp(L, P, S): With L digits of numbers d1, ..., dL, the # of combinations which satisfy (P * product{di}) % (S + sum{di}) = 0
# When L = 0, if P % S return 1, else return 0
# Can be reused for all test cases

def func(L: int, P: int, S: int):
    if (L, P, S) in dp:
        return dp[(L, P, S)]
    elif L == 0:
        dp[(L, P, S)] = int(P % S == 0)
        return dp[(L, P, S)]
    else:
        sum = 0
        for i in range(10): # Append digit 0~9
            sum += func(L - 1, P * i, S + i)
        dp[(L, P, S)] = sum
        return dp[(L, P, S)]

def count_interesting_int(num: int):
    if num < 1:
        return 0

    digits = []
    while num != 0:
        digits.append(num % 10)
        num //= 10
    digits.reverse()
    n = len(digits)

    count = 0
    # Count interesting numbers under 9, 99, 999..., until length n - 1
    for l in range(1, n):
        for i in range(1, 10): # First digit cannot be 0, so iterate 1~9 here and call func for the rest
            count += func(l - 1, i, i)
    
    # Count interesting numbers between 10^n ~ num
    # e.g. num = 54323, count 10000~49999, 5|0000~5|3999, 54|000~54|299, 543|00~543|19, 5432|0~5432|2, 54323
    P = 1
    S = 0
    for l in range(0, n):
        if l == 0:
            start = 1 # First digit cannot be 0, so start from 1
        else:
            start = 0
        for i in range(start, digits[l]):
            # print(n - l - 1, P * i, S + i, func(n - l - 1, P * i, S + i))
            count += func(n - l - 1, P * i, S + i)
        P *= digits[l]
        S += digits[l]
    # Check num itself
    if S > 0 and P % S == 0:
        count += 1
    return count

T = int(input())
for t in range(T):
    [A, B] = [int(x) for x in input().split()]

    ans = count_interesting_int(B) - count_interesting_int(A - 1)
    print(f"Case #{t + 1}: {ans}")
