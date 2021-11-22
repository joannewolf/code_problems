# Painter
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435914/00000000008d9a88

T = int(input())
for t in range(T):
    N = int(input())
    P = input()

    yellow = [False] * (N + 1)
    red = [False] * (N + 1)
    blue = [False] * (N + 1)
    for i, c in enumerate(P):
        if c == 'Y':
            yellow[i] = True
        elif c == 'R':
            red[i] = True
        elif c == 'B':
            blue[i] = True
        elif c == 'O':
            yellow[i] = True
            red[i] = True
        elif c == 'P':
            red[i] = True
            blue[i] = True
        elif c == 'G':
            yellow[i] = True
            blue[i] = True
        elif c == 'A':
            yellow[i] = True
            red[i] = True
            blue[i] = True
    # print(yellow)
    # print(red)
    # print(blue)

    ans = 0
    for i in range(1, N + 1):
        if yellow[i] == False and yellow[i - 1] == True:
            ans += 1
        if red[i] == False and red[i - 1] == True:
            ans += 1
        if blue[i] == False and blue[i - 1] == True:
            ans += 1

    print(f"Case #{t + 1}: {ans}")
