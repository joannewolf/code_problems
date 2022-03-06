# Diagonal Puzzle
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050edd/00000000001a2835
# The problem can be converted to variant of 2-coloring
# Each cell is shared by two diagonals, if it's white, either one of the diagonal needs to be flipped
# Consider each diagonal as vertex, and the shared cell as edge connected two vertex
# If cell is white initially, the vertice are colored differently initially; if black, same color initially
# Final goal is to make all edges having endpoint vertices with same color, and with minimum flips, flips means toggle color of vertex
# For example, N = 4
#  3456          0123
# 2 \\\\        ////4
# 1 \\\\        ////5
# 0 \\\\        ////6
#   \\\\        ////
# c-r+(N-1)=0~6 c+r=0~6
T = int(input())
for t in range(T):
    N = int(input())
    grid = []
    for _ in range(N):
        row = [c == '#' for c in input()] # True is black, False is white
        grid.append(row)

    V = (2 * N - 1) * 2 # 0 ~ 2N-2 for \; 2N-1 ~ 4N-3 for /
    graph = [[] for _ in range(V)]
    color = [0] * V # Color 1 vs. -1, 0 means undecided
    for r in range(N):
        for c in range(N):
            # For each cell...
            v = c - r + (N - 1) # Which \ diagonal it belongs to
            w = c + r + (2 * N - 1) # Which / diagonal it belongs to
            graph[v].append(w)
            graph[w].append(v)
    # for i in range(V):
    #     print(graph[i])
    
    # Since N >= 2, we can initialize the color of \ diagonal which contains cell (0, 0) and (0, 1)
    # Then determine rest diagonal vertex color correspondingly
    unchecked = set(range(V))
    color[0 - 0 + (N - 1)] = 1
    color[1 - 0 + (N - 1)] = 1
    queue = [N - 1, N]
    while queue:
        v = queue.pop(0)
        if v in unchecked:
            # print("remove", v)
            unchecked.remove(v)
            for w in graph[v]:
                r = (abs(w - v) - N) // 2
                c = (v + w + 2 - 3 * N) // 2
                # print("v", v, "w", w, "r", r, "c", c)
                if grid[r][c]: # Black edge, same color on endpoint vertices
                    color[w] = color[v]
                else: # White edge, different color on endpoint vertices
                    color[w] = -color[v]
                if w in unchecked:
                    queue.append(w)
    # print(color)

    ans = 0
    # Count all relative diagonals of cell (0, 0)
    count1 = 0 # Count of vertex with color 1
    count2 = 0 # Count of vertex with color -1
    checked = set()
    queue = [N - 1]
    while queue:
        v = queue.pop(0)
        if v not in checked:
            checked.add(v)
            if color[v] == 1:
                count1 += 1
            else:
                count2 += 1
        for w in graph[v]:
            if w not in checked:
                queue.append(w)
    # print(count1, count2)
    ans += min(count1, count2)

    # Count all relative diagonals of cell (0, 1)
    count1 = 0 # Count of vertex with color 1
    count2 = 0 # Count of vertex with color -1
    checked = set()
    queue = [N]
    while queue:
        v = queue.pop(0)
        if v not in checked:
            checked.add(v)
            if color[v] == 1:
                count1 += 1
            else:
                count2 += 1
        for w in graph[v]:
            if w not in checked:
                queue.append(w)
    # print(count1, count2)
    ans += min(count1, count2)

    print(f"Case #{t + 1}: {ans}")
