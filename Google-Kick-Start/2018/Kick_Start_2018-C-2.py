# Fairies and Witches
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050ee0/0000000000051132
# TLE but correct locally on test set 2

# Check whether i-th bit is 1 or not
def bit(mask: int, i: int):
    return (mask >> i) & 1

def is_good_polygon(edges: list):
    if len(edges) < 3:
        return False
    else:
        # In order to form a polygon, sum of all other edges > max edge
        return sum(edges) - max(edges) > max(edges)

def solve(mask: int, edges: list):
    if mask + 1 == (1 << N): # mask = 1111... all bit 1, i.e. all nodes used
        return is_good_polygon(edges)
    else:
        res = 0
        for i in range(N):
            if not bit(mask, i): # If node i = 0, i.e. unused
                res += solve(mask | (1 << i), edges) # Skip node i and directly mark it used
                for j in range(i + 1, N):
                    if not bit(mask, j) and grid[i][j] != 0: # Use edge(i, j)
                        res += solve(mask | (1 << i) | (1 << j), edges + [grid[i][j]])
                break
        return res

T = int(input())
for t in range(T):
    N = int(input())
    grid = []
    for _ in range(N):
        row = [int(x) for x in input().split()]
        grid.append(row)

    print(f"Case #{t + 1}: {solve(0, [])}")
