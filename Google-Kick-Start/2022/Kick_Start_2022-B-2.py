# Palindromic Factors
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000008caa74/0000000000acee89

import math

def is_palindrome(num: int):
    num = str(num)
    n = len(num)
    for i in range(n // 2):
        if num[i] != num[n - i - 1]:
            return False
    return True

T = int(input())
for t in range(T):
    num = int(input())

    ans = 0
    for i in range(1, int(math.sqrt(num)) + 1):
        if num % i == 0:
            if is_palindrome(i):
                ans += 1
            if num // i != i and is_palindrome(num // i):
                ans += 1

    print(f"Case #{t + 1}: {ans}")
