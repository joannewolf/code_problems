# Stable Wall
# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff43/00000000003379bb

def add_to_dict(key, dict, i, j):
    if key in dict:
        dict[key].append((i, j))
    else:
        dict[key] = [(i, j)]

def is_supported(key):
    supported = True
    for (i, j) in bottom[key]:
        if not(i == R - 1 or board[i + 1][j] in used):
            supported = False
            break
    return supported

T = int(input())
for t in range(T):
    [R, C] = [int(n) for n in input().split()]
    board = []
    for i in range(R):
        board.append(input())

    not_used = set()
    used = set()
    bottom = {}
    # Dict for all under-facing cells
    for i in range(R):
        for j in range(C):
            not_used.add(board[i][j])
            if i == R - 1:
                add_to_dict(board[i][j], bottom, i, j)
            elif board[i][j] != board[i + 1][j]:
                add_to_dict(board[i][j], bottom, i, j)
    # print(not_used)
    # for key in bottom.keys():
    #     print(key, bottom[key])

    ans = ""
    while not_used:
        no_new_supported = True
        for key in not_used:
            if is_supported(key):
                ans += key
                used.add(key)
                no_new_supported = False
        if no_new_supported:
            break
        else:
            not_used -= used
        # print(not_used, used)

    if not_used:
        print(f"Case #{t + 1}: -1")
    else:
        print(f"Case #{t + 1}: {ans}")
