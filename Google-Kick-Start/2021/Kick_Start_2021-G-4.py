# Simple Polygon
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000004362d6/00000000008b36f9
# Create zig-zag shape with each section height = 1, so only need to control top and bottom width
# When N is odd number, it will become 2, 2, ..., 1 dots from left to right
# And total area can be written as (a1 + a2) + (a2 + a3) + ... + (a_{N/2-1} + a_{N/2}) + a_{N/2} = A
# When N is even number, it will become 2, 2, ..., 2 dots from left to right
# And total area can be written as (a1 + a2) + (a2 + a3) + ... + (a_{N/2-1} + a_{N/2}) = A
# Let a2 ~ a_{N/2} all be 1, and a1 handle the remain number

T = int(input())
for t in range(T):
    [N, A] = [int(n) for n in input().split()]

    if A < (N // 2 - 1) * 2 + (N % 2):
        print(f"Case #{t + 1}: IMPOSSIBLE")
    else:
        print(f"Case #{t + 1}: POSSIBLE")
        remain = A - ((N // 2 - 1) * 2 + (N % 2) - 1)
        if remain != 3:
            print("0 0")
        else:
            # To prevent from two edge are on the same straight line
            print("0 1")
        for i in range(1, (N + 1) // 2):
            print(f"{i} {i % 2}")
        for i in range((N - 2) // 2, 0, -1):
            print(f"{i} {i % 2 + 1}")
        if remain != 3:
            print(f"0 {remain}")
        else:
            print(f"0 {remain + 1}")
