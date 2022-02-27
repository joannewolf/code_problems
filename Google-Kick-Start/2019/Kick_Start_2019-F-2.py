# Teach Me
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050edc/00000000001864bc
# Brute-force, O(N^2), TLE on test set 2

T = int(input())
for t in range(T):
    [N, S] = map(int, input().split())
    skills = []
    for i in range(N):
        s = [int(x) for x in input().split()]
        skills.append(set(s[1:]))

    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            for s in skills[i]:
                if s not in skills[j]:
                    ans += 1
                    break
            for s in skills[j]:
                if s not in skills[i]:
                    ans += 1
                    break

    print(f"Case #{t + 1}: {ans}")
