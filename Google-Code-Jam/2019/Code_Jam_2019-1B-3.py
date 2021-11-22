# Fair Fight
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000051706/0000000000122838
# Use DP, O(N^2), pass test set 1

T = int(input())
for t in range(T):
    [N, K] = [int(n) for n in input().split()]
    skill_C = [int(n) for n in input().split()]
    skill_D = [int(n) for n in input().split()]

    # max_C[i][j]: the max skill level between i and j swords (inclusive)
    max_C = [[0] * N for i in range(N)]
    max_D = [[0] * N for i in range(N)]
    for i in range(N):
        max_C[i][i] = skill_C[i]
        max_D[i][i] = skill_D[i]
        for j in range(i + 1, N):
            max_C[i][j] = skill_C[j] if (skill_C[j] > max_C[i][j - 1]) else max_C[i][j - 1]
            max_D[i][j] = skill_D[j] if (skill_D[j] > max_D[i][j - 1]) else max_D[i][j - 1]

    result = 0
    for i in range(N):
        for j in range(i, N):
            if abs(max_C[i][j] - max_D[i][j]) <= K:
                result += 1

    print("Case #{}: {}".format(t + 1, result))
