# Book Reading
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050e02/000000000018fd0d
# O(MQ), TLE on test set 2

T = int(input())
for t in range(T):
    [N, M, Q] = [int(x) for x in input().split()]
    pages = [int(x) for x in input().split()]
    readers = [int(x) for x in input().split()]

    ans = 0
    for r in readers:
        count = 0
        for p in pages:
            if p % r == 0:
                count += 1
        ans += N // r - count

    print(f"Case #{t + 1}: {ans}")
