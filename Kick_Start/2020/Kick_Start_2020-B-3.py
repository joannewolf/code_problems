# Robot Path Decoding
# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ffc8/00000000002d83dc

T = int(input())
for t in range(T):
    program = input()
    stack = [[1, 1, 1]] # [repeat_time, move_x, move_y]

    for c in program:
        if c == 'E':
            stack[-1][1] += 1
        elif c == 'W':
            stack[-1][1] -= 1
        elif c == 'N':
            stack[-1][2] -= 1
        elif c == 'S':
            stack[-1][2] += 1
        elif c.isdigit():
            stack.append([int(c), 0, 0])
        elif c == ')':
            last_move = stack.pop(-1)
            stack[-1][1] += last_move[0] * last_move[1]
            stack[-1][2] += last_move[0] * last_move[2]

    final_x = (stack[0][1] + pow(10, 9)) % pow(10, 9)
    if final_x == 0:
        final_x = pow(10, 9)
    final_y = (stack[0][2] + pow(10, 9)) % pow(10, 9)
    if final_y == 0:
        final_y = pow(10, 9)
    print(f"Case #{t + 1}: {final_x} {final_y}")
