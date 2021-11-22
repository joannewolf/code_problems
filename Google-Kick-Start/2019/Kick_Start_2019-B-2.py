# Energy Stones
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050eda/00000000001198c3
# DP, O(2^N), TLE on test set 1

# When a stone is put last, the energy we can get from that stone doesn't matter with the order of all other previous stones
# From remaining stones, pick one as the last one and find what's the best choice to get max energy
# dp_key: N bits number indicating which stones has been chosen so far
def get_energy(stones, dp_key, sum_S):
    if dp[dp_key] != -1:
        return dp[dp_key]

    if len(stones) == 1:
        dp[dp_key] = stones[0][2]
        return stones[0][2]
    else:
        max_energy = 0
        for (i, s, e, l) in stones:
            new_stones = stones.copy()
            new_stones.remove((i, s, e, l))
            energy = max(e - (sum_S - s) * l, 0)+ get_energy(new_stones, dp_key + pow(2, i), sum_S - s)
            max_energy = max(max_energy, energy)
        dp[dp_key] = max_energy
        return max_energy

T = int(input())
for t in range(T):
    N = int(input())
    stones = []
    sum_S = 0
    for i in range(N):
        [s, e, l] = [int(n) for n in input().split()]
        stones.append((i, s, e, l))
        sum_S += s

    dp = [-1] * pow(2, N)
    print(f"Case #{t + 1}: {get_energy(stones, 0, sum_S)}")
