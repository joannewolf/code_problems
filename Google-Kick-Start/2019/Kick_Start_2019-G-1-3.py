# Book Reading
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050e02/000000000018fd0d
# O(NlogN + Q), when computing count[], it's doing N + N/2 + ... + N/N = N(1 + 1/2 + ... + 1/N) ~= NlogN

T = int(input())
for t in range(T):
    [N, M, Q] = [int(x) for x in input().split()]
    pages = set(int(x) for x in input().split())
    readers = [int(x) for x in input().split()]

    count = [0] * (N+1)
    for i in range(1, N+1):
        for j in range(1, N // i + 1):
            if i * j not in pages:
                count[i] += 1

    ans = 0
    for r in readers:
        ans += count[r]

    print(f"Case #{t + 1}: {ans}")
