# Energy Stones
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050eda/00000000001198c3
# Assume we never eat stones with 0 energy, from the remaining eaten stones, there exists a optimal order
# Consider stones i, j, if eating stone i first, energy loss is SiLj; while eating stone j first, energy loss is SjLi
# So if SiLj < SjLi => Si/Li < Sj/Lj, stone i should be eaten first, be careful when Li = 0
# Use this relationship to sort all stones, and then find out which set of stones eaten will give us max energy
# It reduces to 0/1 Knapsack problem https://en.wikipedia.org/wiki/Knapsack_problem
# DP, O(N*sum(S))

# Get max energy given current time and consider only stones i...N
def get_energy(time, i):
    if i == N:
        return 0
    if (time, i) in dp:
        return dp[(time, i)]

    (s, e, l) = stones[i]
    # Take stone i
    option1 = max(e - time * l, 0) + get_energy(time + s, i + 1)
    # Not take stone i
    option2 = get_energy(time, i + 1)
    dp[(time, i)] = max(option1, option2)
    return max(option1, option2)

T = int(input())
for t in range(T):
    N = int(input())
    stones = []
    l0_stones = []
    for i in range(N):
        [s, e, l] = [int(n) for n in input().split()]
        if l != 0:
            stones.append((s, e, l))
        else:
            l0_stones.append((s, e, l))
    stones = sorted(stones, key=lambda x: x[0]/x[2]) + l0_stones

    dp = {}
    print(f"Case #{t + 1}: {get_energy(0, 0)}")
