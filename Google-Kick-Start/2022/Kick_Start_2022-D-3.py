# Touchbar Typing
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000008caea6/0000000000b76f44

T = int(input())
for t in range(T):
    N = int(input())
    word = [int(x) for x in input().split()]
    M = int(input())
    keyboard = [int(x) for x in input().split()]

    ans = 0

    print(f"Case #{t + 1}: {ans}")
