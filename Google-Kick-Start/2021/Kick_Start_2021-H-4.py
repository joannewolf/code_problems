# Dependent Events
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435914/00000000008d9970

T = int(input())
for t in range(T):
    [N, Q] = [int(n) for n in input().split()]
    children = [[] for i in range(N + 1)]
    children[0] = [1]
    K = int(input())
    A = [1, K]
    B = [0, 0]
    for i in range(N - 1):
        [p, a, b] = [int(n) for n in input().split()]
        children[p].append(i + 2)
        A.append(a)
        B.append(b)
    print(children)

    ans = []
    for i in range(Q):
        [u, v] = [int(n) for n in input().split()]

    print(f"Case #{t + 1}: {' '.join([str(n) for n in ans])}")
