# Interesting Outing
# https://codingcompetitions.withgoogle.com/codejamio/round/00000000009d9870/0000000000a33bc7
# O(N^3 + N * N!), TLE but correct locally on test set 1

INF = pow(10, 12) + 1

# Reuse permutation for all test cases, but only for test set 1
permutation = [[] for i in range(11)]
def get_permutation(curr, unused):
    if len(curr) == N:
        permutation[N].append(curr)
    else:
        for num in unused:
            new_unused = unused.copy()
            new_unused.remove(num)
            get_permutation(curr + [num], new_unused)

T = int(input())
for t in range(T):
    N = int(input())
    dist = [[INF] * N for _ in range(N)]
    for _ in range(N - 1):
        [A, B, C] = [int(x) for x in input().split()]
        dist[A - 1][B - 1] = C
        dist[B - 1][A - 1] = C
    for i in range(N):
        dist[i][i] = 0

    # There's only one way for each sight to visit another
    # Use Floyd-Warshal algorithm to compute distance of all pairs of sights
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    # for i in range(N):
    #     print(dist[i])

    # Get all permutation of visiting sights
    if not permutation[N]:
        get_permutation([], list(range(N)))

    ans = INF
    for order in permutation[N]:
        sum = 0
        for i in range(N - 1):
            sum += dist[order[i]][order[i+1]]
        if sum < ans:
            ans = sum
    print(f"Case #{t + 1}: {ans}")
