# Graph Travel
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435bae/0000000000888764
# Find all possible permutations to reach K points, and evaluate whether they are legit
# Use bit to represent rooms, 2^N combinations, O(2^N * N)

def is_path_legit(path: int, point: int, next: int):
    if path == 0:
        return True
    else:
        return L[next] <= point and point <= R[next] and connected[path][next]

def check_all_perms(prefix: int, point: int, rest: int):
    # print(prefix, point, rest)
    if rest == 0:
        return 1
    result = 0
    rest_num = rest
    for i in range(N):
        if rest_num % 2 and is_path_legit(prefix, point, i):
            result += check_all_perms(prefix + pow(2, i), point + A[i], rest - pow(2, i))
        rest_num //= 2
    return result

T = int(input())
for t in range(T):
    [N, M, K] = [int(n) for n in input().split()]
    L = []
    R = []
    A = []
    for i in range(N):
        [l, r, a] = [int(n) for n in input().split()]
        L.append(l)
        R.append(r)
        A.append(a)
    corridor = [0] * N
    for i in range(M):
        [x, y] = [int(n) for n in input().split()]
        corridor[x] += pow(2, y)
        corridor[y] += pow(2, x)
    # print(corridor)

    # For each room combination, no matter if they are connected, get total points
    point = [0] * pow(2, N)
    for i in range(pow(2, N)):
        num = i
        for j in range(N):
            if num % 2:
                point[i] += A[j]
            num //= 2
    # print(point)

    connected = [[False] * N for i in range(pow(2, N))]
    connected[0] = [True] * N
    # connected[i][j] = True means with room combination i visited, can enter room j next
    for i in range(pow(2, N)):
        num = i
        for j in range(N):
            if i & corridor[j] and L[j] <= point[i] and point[i] <= R[j]: 
            # If any bit is overlapped, means room j is connected to some room in combination i
                connected[i][j] = True
            num //= 2
    # for c in connected:
    #     print(c)

    combination = [0] * pow(2, N)
    combination[0] = 1
    # Use dp, combination[i]: the number of legit permutation using room combination i
    for i in range(1, pow(2, N)):
        num = i
        for j in range(N):
            if num % 2 and connected[i - pow(2, j)][j]:
            # For each room in combination i, take it as last room, check if rest room combination can connect to it
                combination[i] += combination[i - pow(2, j)]
            num //= 2
    # print(combination)

    result = 0
    for i in range(pow(2, N)):
        if point[i] == K:
            result += combination[i]

    print(f"Case #{t + 1}: {result}")
