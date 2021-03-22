# https://codingcompetitions.withgoogle.com/codejam/round/0000000000051705/00000000000881da

T = input()
for t in range(int(T)):
    N = int(input())
    path = input()
    result_path = ""
    for c in path:
        if c == 'E':
            result_path += 'S'
        elif c == 'S':
            result_path += 'E'
    print("Case #{}: {}".format(t + 1, result_path))
