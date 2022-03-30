# Palindromic Sequence
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050e07/0000000000051186
# Ref:
# https://blog.csdn.net/lemonmillie/article/details/95203060

import math

ascii_a = ord('a')

def is_palindrome(s: str):
    n = len(s)
    for i in range(n // 2):
        if s[i] != s[n - 1 - i]:
            return False
    return True

# P(S): # of palindromes that have S as a prefix, P(S) = SUM{P(S, l)}, l = len(S)~N
def P(prefix: str):
    count = 0
    n = len(prefix)
    for l in range(n, N + 1):
        if (l + 1) // 2 >= n: # Whole prefix is in first half of palindrome, rest spaces can put any letter
            rest = (l + 1) // 2 - n
            count += pow(L, rest)
        elif is_palindrome(prefix[l - n:]):
            count += 1
    return count

T = int(input())
for t in range(T):
    [L, N, K] = [int(x) for x in input().split()]

    ans = 0

    if K <= N: # String with K a's
        ans = K
    elif L == 1: # No more letter to produce palindrome > N
        ans = 0
    else:
        a = int((N + 1) // 2 - math.log(K, L)) # How many a's in head and tail
        if a < 0:
            ans = 0
        else:
            N -= (a * 2)
            K -= (a * 2)
            prefix = ""
            while True:
                count = int(is_palindrome(prefix))
                if count <= K:
                    K -= count
                else:
                    ans = len(prefix) + (a * 2)
                    break
                no_more_letter = True
                for i in range(L): # Iterate possible letter for next char in prefix
                    c = chr(ascii_a + i)
                    count = P(prefix + c)
                    if count <= K:
                        K -= count
                    else:
                        prefix += c
                        no_more_letter = False
                        break
                if no_more_letter:
                    ans = 0
                    break

    print(f"Case #{t + 1}: {ans}")
