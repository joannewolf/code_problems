# Imbalance Obviation
# https://codingcompetitions.withgoogle.com/codejamio/round/000000000019ff03/00000000001b5cd7

T = raw_input()
for t in xrange(int(T)):
    N = int(raw_input())
    A = [int(a) for a in raw_input().split(' ')]
    ans = []
    pair = {}

    if N % 2 == 1:
        A.insert(0, N + 1)
        ans = ['X'] * (N + 2)
    else:
        ans = ['X'] * (N + 1)

    # pair (A1, A2), (A3, A4), ..., and each pair has to be one L and one R
    # also pair (1, 2), (3, 4), ..., and each pair has to be one L and one R
    for i in range(1, len(ans), 2):
        pair[i] = {i + 1}
        pair[i + 1] = {i}
    
    for i in range(0, len(A), 2):
        pair[A[i]].add(A[i + 1])
        pair[A[i + 1]].add(A[i])

    toBeChecked = []
    while pair:
        if not toBeChecked:
            currentKey = pair.keys()[0]
            ans[currentKey] = 'L'
            for value in pair[currentKey]:
                ans[value] = 'R'
            toBeChecked.extend(pair[currentKey])
            pair.pop(currentKey)
        else:
            currentKey = toBeChecked.pop(0)
            for value in pair[currentKey]:
                if ans[value] == 'X':
                    ans[value] = 'L' if ans[currentKey] == 'R' else 'R'
                    toBeChecked.append(value)
            pair.pop(currentKey)

    print "Case #{}: {}".format(t + 1, ''.join(ans[1 : N + 1]))