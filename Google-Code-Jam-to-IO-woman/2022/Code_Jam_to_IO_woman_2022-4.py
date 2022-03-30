# Inventor Outlasting
# https://codingcompetitions.withgoogle.com/codejamio/round/00000000009d9870/0000000000a33fb0

T = int(input())
for t in range(T):
    [R, C] = [int(x) for x in input().split()]
    board = []
    for _ in range(R):
        board.append(input())

    ans = 0

    print(f"Case #{t + 1}: {ans}")
