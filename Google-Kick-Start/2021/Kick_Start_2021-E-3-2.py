# Palindromic Crossword
# https://codingcompetitions.withgoogle.com/kickstart/round/000000000043585c/0000000000859dcd
# Categorize each cell into classes such that same class are having the same char
# Then iterate each class to fill the char, O(N * M) to build graph and iterate nodes by BFS

def add_edge(graph: dict, r1, c1, r2, c2):
    if (r1, c1) not in graph:
        graph[(r1, c1)] = [(r2, c2)]
    else:
        graph[(r1, c1)].append((r2, c2))
    if (r2, c2) not in graph:
        graph[(r2, c2)] = [(r1, c1)]
    else:
        graph[(r2, c2)].append((r1, c1))

T = int(input())
for t in range(T):
    [N, M] = [int(n) for n in input().split()]
    crossword = []
    for i in range(N):
        crossword.append(list(input()))

    graph = {}
    flag = -1
    for i in range(N):
        for j in range(M):
            if crossword[i][j] != '#' and flag == -1:
                flag = j
            elif crossword[i][j] == '#' and flag != -1:
                for k in range((j - flag) // 2):
                    add_edge(graph, i, flag + k, i, j - k - 1)
                flag = -1
        if flag != -1:
            for k in range((M - flag) // 2):
                add_edge(graph, i, flag + k, i, M - k - 1)
        flag = -1

    for j in range(M):
        for i in range(N):
            if crossword[i][j] != '#' and flag == -1:
                flag = i
            elif crossword[i][j] == '#' and flag != -1:
                for k in range((i - flag) // 2):
                    add_edge(graph, flag + k, j, i - k - 1, j)
                flag = -1
        if flag != -1:
            for k in range((N - flag) // 2):
                add_edge(graph, flag + k, j, N - k - 1, j)
        flag = -1
    # print(graph)

    result = 0
    checked = [[False] * M for i in range(N)]
    for i in range(N):
        for j in range(M):
            if crossword[i][j] != '#' and crossword[i][j] != '.' and not checked[i][j]:
                # BFS to iterate all cells in same class
                stack = [(i, j)]
                while stack:
                    (current_i, current_j) = stack.pop(0)
                    checked[current_i][current_j] = True
                    if (current_i, current_j) in graph:
                        for (next_i, next_j) in graph[(current_i, current_j)]:
                            if crossword[next_i][next_j] == '.':
                                result += 1
                                crossword[next_i][next_j] = crossword[current_i][current_j]
                            if not checked[next_i][next_j]:
                                stack.append((next_i, next_j))

    print(f"Case #{t + 1}: {result}")
    for i in range(N):
        print("".join(crossword[i]))