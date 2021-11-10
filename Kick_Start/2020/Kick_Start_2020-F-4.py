# Yeetzhee
# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff48/00000000003f4dea
# Using recursion + DP, explanation http://www.thetechjarvis.com/google-kickstart-round-f-2020-solution-yeetzhee/
# State: list of size M with non-decreasing number, representing the count of different type of dice number
# initial state: [0] * M; sum(target state) = N
# If a state's each number <= target state's each number, then it's a valid state
# e.g. N = 3, M = 6, With target state (0, 0, 0, 0, 1, 2); (0, 0, 0, 0, 0, 1) is valid, (0, 0, 0, 1, 1, 1) is invalid, (0, 0, 0, 0, 2, 1) should not appear
# E(state) = (Average Rolls at state) + SUM{p(next_valid_state) * E(next_valid_state)}
#   = M / total_valid_count + SUM{count(next_valid_state) / total_valid_count * E(next_valid_state)}
#   Average Rolls = 1 / p(get valid dice number)

def throw(state):
    # print("state", state)
    if sum(state) == N:
        return 0
    if tuple(state) in dp:
        return dp[tuple(state)]

    result = 0
    count = 0
    valid_count = 0
    for i in range(M):
        if i == 0 or state[i] == state[i - 1]:
            count += 1
        if i == M - 1 or state[i] != state[i + 1]:
            if state[i] < target[i]: # Valid next state
                state[i] += 1
                valid_count += count
                result += throw(tuple(state)) * count
                state[i] -= 1
            count = 1

    result = M / valid_count + result / valid_count
    dp[tuple(state)] = result
    return result

T = int(input())
for t in range(T):
    [N, M, K] = [int(n) for n in input().split()]
    target = [0] * (M - K)
    for i in range(K):
        target.append(int(input()))

    dp = {}
    initial = [0] * M

    print(f"Case #{t + 1}: {throw(initial)}")
