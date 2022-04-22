# X Squared
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000201c98/0000000000201b7a

def add_map(map: map, key: tuple):
    if key not in map:
        map[key] = 1
    else:
        map[key] += 1

T = int(input())
for t in range(T):
    N = int(input())
    grid = []
    for _ in range(N):
        grid.append(input())


    ans = True
    pair = {}
    for r in range(N):
        index = []
        for c in range(N):
            if grid[r][c] == 'X':
                index.append(c)
        if len(index) == 0 or len(index) > 2:
            ans = False
            break
        if len(index) == 2:
            add_map(pair, tuple(index))
    for (_, value) in pair.items():
        if value != 2:
            ans = False

    pair = {}
    for c in range(N):
        index = []
        for r in range(N):
            if grid[r][c] == 'X':
                index.append(r)
        if len(index) == 0 or len(index) > 2:
            ans = False
            break
        if len(index) == 2:
            add_map(pair, tuple(index))
    for (_, value) in pair.items():
        if value != 2:
            ans = False

    if ans:
        print(f"Case #{t + 1}: POSSIBLE")
    else:
        print(f"Case #{t + 1}: IMPOSSIBLE")
