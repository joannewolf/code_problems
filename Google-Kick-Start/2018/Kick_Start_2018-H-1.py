# Big Buttons
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050ee2/0000000000051136

T = int(input())
for t in range(T):
    [N, P] = [int(x) for x in input().split()]
    prefix = []
    for _ in range(P):
        prefix.append(input())

    # Remove duplicate prefix that will be covered by others
    duplicate = set()
    for i in range(P):
        for j in range(i+1, P):
            if len(prefix[i]) < len(prefix[j]) and prefix[j][0:len(prefix[i])] == prefix[i]:
                duplicate.add(prefix[j])
            elif len(prefix[j]) < len(prefix[i]) and prefix[i][0:len(prefix[j])] == prefix[j]:
                duplicate.add(prefix[i])
    # print(duplicate)

    ans = pow(2, N)
    for p in prefix:
        if p not in duplicate:
            ans -= pow(2, N - len(p))

    print(f"Case #{t + 1}: {ans}")
