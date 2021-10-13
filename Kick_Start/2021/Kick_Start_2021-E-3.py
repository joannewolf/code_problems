# Palindromic Crossword
# https://codingcompetitions.withgoogle.com/kickstart/round/000000000043585c/0000000000859dcd
# Iterate all word until we cannot find any more char to fill, TLE on test set 2

def make_palindrome(str):
    count = 0
    N = len(str)
    for i in range(N // 2):
        if str[i] != str[N - i - 1]:
            count += 1
            if str[i] == '.':
                str[i] = str[N - i - 1]
            else:
                str[N - i - 1] = str[i]

    return count, str

T = int(input())
for t in range(T):
    [N, M] = [int(n) for n in input().split()]
    crossword = []
    for i in range(N):
        crossword.append(list(input()))

    row_palindrome = [[] for i in range(N)]
    col_palindrome = [[] for i in range(M)]
    flag = -1
    for i in range(N):
        for j in range(M):
            if crossword[i][j] != '#' and flag == -1:
                flag = j
            elif crossword[i][j] == '#' and flag != -1:
                row_palindrome[i].append((flag, j - 1))
                flag = -1
        if flag != -1:
            row_palindrome[i].append((flag, M - 1))
        flag = -1

    for j in range(M):
        for i in range(N):
            if crossword[i][j] != '#' and flag == -1:
                flag = i
            elif crossword[i][j] == '#' and flag != -1:
                col_palindrome[j].append((flag, i - 1))
                flag = -1
        if flag != -1:
            col_palindrome[j].append((flag, N - 1))
        flag = -1

    # for i in range(N):
    #     print(row_palindrome[i])
    # print()
    # for i in range(M):
    #     print(col_palindrome[i])

    result = 0
    while True:
        no_change = True
        for i in range(N):
            for (l, r) in row_palindrome[i]:
                [num, str] = make_palindrome(crossword[i][l: r + 1])
                if num != 0:
                    no_change = False
                    result += num
                    crossword[i][l: r + 1] = str
        for j in range(M):
            for (u, d) in col_palindrome[j]:
                [num, str] = make_palindrome([row[j] for row in crossword[u: d + 1]])
                if num != 0:
                    no_change = False
                    result += num
                    for i in range(u, d + 1):
                        crossword[i][j] = str[i - u]
        if no_change:
            break

    print(f"Case #{t + 1}: {result}")
    for i in range(N):
        print("".join(crossword[i]))