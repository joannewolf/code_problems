# Workout
# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ffc7/00000000001d3f5b
# Find d' such that all gap can be divided equally the most
# d1 / (k1 + 1) ~= d2 / (k2 + 1) ..., k1 + k2 + ... = K
# O(log(10^9))

def get_needed_training(target):
    count = 0
    for d in diff:
        if d % target == 0:
            count += (d // target - 1)
        else:
            count += (d // target)
    return count

T = int(input())
for t in range(T):
    [N, K] = [int(n) for n in input().split()]
    exercise = [int(n) for n in input().split()]

    diff = []
    for i in range(1, N):
        temp = exercise[i] - exercise[i - 1]
        diff.append(temp)

    # Use binary search to find the best d', and how many addition needed for that d'; when d' is smaller, bigger addition exercises needed
    # Eventually find the min d' such that K >= needed addition
    L = 1
    R = pow(10, 9)
    while L <= R:
        mid = (L + R) // 2
        if get_needed_training(mid) <= K:
            R = mid - 1
        else:
            L = mid + 1

    print(f"Case #{t + 1}: {L}")
