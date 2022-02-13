# Food Stalls
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000051061/0000000000161476
# O(N^2logN), TLE on test set 2

INT_MAX = pow(10, 15)

T = int(input())
for t in range(T):
    [K, N] = [int(n) for n in input().split()]
    X = [int(n) for n in input().split()]
    C = [int(n) for n in input().split()]

    ans = INT_MAX
    # For each spot, assume we build warehouse there and find the K smallest costs for stalls
    for i in range(N):
        cost = C[i]
        new_C = C.copy()
        for j in range(N):
            new_C[j] += abs(X[i] - X[j])
        new_C.pop(i)
        new_C.sort()
        cost += sum(new_C[0:K])
        if cost < ans:
            ans = cost

    print(f"Case #{t + 1}: {ans}")
