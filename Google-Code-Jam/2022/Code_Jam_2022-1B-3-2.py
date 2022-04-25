# ASeDatAb
# https://codingcompetitions.withgoogle.com/codejam/round/000000000087711b/0000000000acd29b

import sys

MAX_TRY = 299

def appendzero(s):
    return s + '0' * len(s)

def expand(s):
    return s + s

def P(k):
    if k == 0:
        return ['1']
    seq = P(k - 1)
    seq_with_zero = [appendzero(s) for s in seq]
    seq_with_copy = [expand(s) for s in seq]
    res = seq_with_copy[:]
    for ins in seq_with_zero:
        res += [ins]
        res += seq_with_copy
    return res

P3 = P(3)
# for l in P3:
#     print(l)

T = int(input())
for t in range(T):
    for mask in P3:
        print(mask)
        sys.stdout.flush()
        bit = int(input())

        if bit == 0:
            break
