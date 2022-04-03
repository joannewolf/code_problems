# 3D Printing
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000876ff1/0000000000a4672b

T = int(input())
for t in range(T):
    [C1, M1, Y1, K1] = [int(x) for x in input().split()]
    [C2, M2, Y2, K2] = [int(x) for x in input().split()]
    [C3, M3, Y3, K3] = [int(x) for x in input().split()]

    min_C = min(C1, C2, C3)
    min_M = min(M1, M2, M3)
    min_Y = min(Y1, Y2, Y3)
    min_K = min(K1, K2, K3)

    if min_C + min_M + min_Y + min_K < pow(10, 6):
        print(f"Case #{t + 1}: IMPOSSIBLE")
    elif min_C >= pow(10, 6):
        print(f"Case #{t + 1}: {pow(10, 6)} 0 0 0")
    elif min_C + min_M >= pow(10, 6):
        print(f"Case #{t + 1}: {min_C} {pow(10, 6) - min_C} 0 0")
    elif min_C + min_M + min_Y >= pow(10, 6):
        print(f"Case #{t + 1}: {min_C} {min_M} {pow(10, 6) - (min_C + min_M)} 0")
    else:
        print(f"Case #{t + 1}: {min_C} {min_M} {min_Y} {pow(10, 6) - (min_C + min_M + min_Y)}")
