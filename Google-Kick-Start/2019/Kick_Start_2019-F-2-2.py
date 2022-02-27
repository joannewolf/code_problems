# Teach Me
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050edc/00000000001864bc
# m(i) = # of people who can mentor i-th employee, final goal is to find SUM(m(i))
# m(i) = N - # of people who cannot mentor i
# If j cannot mentor i -> skill[j] must be subset of skill[i]
# O(2^5*N), cuz each person knows up to 5 different skills

def add_map(map: map, key):
    if key not in map:
        map[key] = 1
    else:
        map[key] += 1

T = int(input())
for t in range(T):
    [N, S] = map(int, input().split())
    skill_map = {}
    for i in range(N):
        s = [int(x) for x in input().split()]
        add_map(skill_map, tuple(sorted(s[1:])))
    # print(skill_map)

    ans = 0
    for skill in skill_map:
        count = 0
        n = len(skill)
        # print("skill", skill, n)
        # Find all subset of current skill set
        for combination in range(pow(2, n)):
            subset = []
            num = combination
            for i in range(n):
                if num % 2 == 1:
                    subset.append(skill[i])
                num //= 2
            # print(combination, subset)
            if tuple(subset) in skill_map:
                count += skill_map[tuple(subset)]
        ans += (N - count) * skill_map[skill]

    print(f"Case #{t + 1}: {ans}")
