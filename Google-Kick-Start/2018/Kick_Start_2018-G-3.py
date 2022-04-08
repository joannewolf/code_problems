# Cave Escape
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000051066/0000000000051135
# Let N_T = # of traps, O(N * M * 2^N_T + 2^N_T * N_T)
# TLE but correct locally on test set 1

BLOCK = -100000
N_INF = BLOCK * 10000

def get_max_energy(mask: int):
    if max_energy[mask] != N_INF:
        return max_energy[mask]
    # print("in mask", mask)

    res = -1
    if exit[mask]:
        res = energy[mask]

    # Try unvisited reachable trap
    for i in reachable[mask]:
        if energy[mask] >= -cave[traps[i][0]][traps[i][1]]:
            res = max(res, get_max_energy(mask | (1 << i)))
    max_energy[mask] = res

    return res

T = int(input())
for t in range(T):
    [N, M, E, S_R, S_C, T_R, T_C] = [int(x) for x in input().split()]
    S_R -= 1
    S_C -= 1
    T_R -= 1
    T_C -= 1
    cave = []
    for _ in range(N):
        cave.append([int(x) for x in input().split()])

    traps = []
    trap_index = {}
    for r in range(N):
        for c in range(M):
            if cave[r][c] < 0 and cave[r][c] != BLOCK:
                traps.append((r, c))
    N_traps = len(traps)
    for i in range(N_traps):
        trap_index[traps[i]] = i
    # print(trap_index)

    # For all combinations of visited traps, calculate energy, next reachable traps and whether can reach exit
    N_mask = pow(2, N_traps)
    energy = [E] * N_mask
    max_energy = [N_INF] * N_mask
    reachable = [set() for _ in range(N_mask)]
    exit = [False] * N_mask
    for mask in range(N_mask):
        num = mask
        checked = set()
        current_traps = set()
        queue = [(S_R, S_C)]
        for i in range(N_traps):
            if num % 2 == 1:
                queue.append(traps[i])
                current_traps.add(traps[i])
                energy[mask] += cave[traps[i][0]][traps[i][1]]
            num //= 2

        while queue:
            (now_r, now_c) = queue.pop(0)
            if (now_r, now_c) in checked:
                continue
            checked.add((now_r, now_c))
            if now_r == T_R and now_c == T_C:
                exit[mask] = True
                continue
            if (now_r, now_c) not in current_traps and cave[now_r][now_c] < 0:
                reachable[mask].add(trap_index[(now_r, now_c)])
                continue
            if cave[now_r][now_c] > 0:
                energy[mask] += cave[now_r][now_c]

            if now_r != 0 and cave[now_r - 1][now_c] != BLOCK and (now_r - 1, now_c) not in checked:
                queue.append((now_r - 1, now_c))
            if now_r != N - 1 and cave[now_r + 1][now_c] != BLOCK and (now_r + 1, now_c) not in checked:
                queue.append((now_r + 1, now_c))
            if now_c != 0 and cave[now_r][now_c - 1] != BLOCK and (now_r, now_c - 1) not in checked:
                queue.append((now_r, now_c - 1))
            if now_c != M - 1 and cave[now_r][now_c + 1] != BLOCK and (now_r, now_c + 1) not in checked:
                queue.append((now_r, now_c + 1))
        # print("mask", format(mask, f'#0{N_traps+2}b'), mask, "energy", energy[mask], "reachable", reachable[mask], "exit", exit[mask])

    print(f"Case #{t + 1}: {get_max_energy(0)}")
