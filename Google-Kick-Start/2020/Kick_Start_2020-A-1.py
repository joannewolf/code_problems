# Allocation
# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ffc7/00000000001d3f56

T = int(input())
for t in range(T):
    [N, B] = [int(n) for n in input().split()]
    house = [int(n) for n in input().split()]

    house.sort()

    result = 0
    for h in house:
        if B >= h:
            B -= h
            result += 1
        else:
            break

    print(f"Case #{t + 1}: {result}")
