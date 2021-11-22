# Merge Cards
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000001a0069/0000000000415054
# Pre-compute the constant of A1, A2, ..., A_N, O(N^2) to compute all constants
# O(N) for each test to sum up the answer

constant = [[] for i in range(2)]
constant.append([1, 1])

def expand_constant(N):
    for n in range(len(constant), N + 1):
        temp_constant = [0] * n
        # Iterate n - 1 types of merge, and multiply with previous constant
        for i in range(n - 1):
            temp_constant[i] += 1
            temp_constant[i + 1] += 1
            for j in range(i):
                temp_constant[j] += constant[-1][j]
            temp_constant[i] += constant[-1][i]
            temp_constant[i + 1] += constant[-1][i]
            for j in range(i + 2, n):
                temp_constant[j] += constant[-1][j - 1]
        # Each merge are equally possible to occur, so expected value divided by n-1
        for i in range(n):
            temp_constant[i] /= (n - 1)

        constant.append(temp_constant)

T = int(input())
for t in range(T):
    N = int(input())
    nums = [int(n) for n in input().split()]

    if N > len(constant) - 1:
        expand_constant(N)

    ans = 0
    for i in range(N):
        ans += constant[N][i] * nums[i]

    print(f"Case #{t + 1}: {ans}")
