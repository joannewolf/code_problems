# King's Circle
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050ff4/00000000000510ee
# Key idea: If using two points to form a bounding box, then they can form valid triplet with any point NOT strictly inside the bounding box
# For any invalid triplet, exactly one of the points will be inside the bounding box defined by the other two points
# O(N^2), TLE on test set 2

T = int(input())
for t in range(T):
    [N, V1, H1, A, B, C, D, E, F, M] = [int(x) for x in input().split()]
    cafes = [(V1, H1)]
    for i in range(1, N):
        V2 = (A * V1 + B * H1 + C) % M
        H2 = (D * V1 + E * H1 + F) % M
        cafes.append((V2, H2))
        V1, H1 = V2, H2
    # print(cafes)

    invalid = 0
    # For each point, count its upper-left * lower-right and upper-right * lower-left points
    # And count the combination number to form bounding box around it
    for i in range(N):
        upper_left = 0
        upper_right = 0
        lower_left = 0
        lower_right = 0
        for j in range(N):
            if cafes[j][0] < cafes[i][0] and cafes[j][1] < cafes[i][1]:
                upper_left += 1
            elif cafes[j][0] < cafes[i][0] and cafes[j][1] > cafes[i][1]:
                upper_right += 1
            elif cafes[j][0] > cafes[i][0] and cafes[j][1] < cafes[i][1]:
                lower_left += 1
            elif cafes[j][0] > cafes[i][0] and cafes[j][1] > cafes[i][1]:
                lower_right += 1
        invalid += (upper_left * lower_right + upper_right * lower_left)

    ans = N * (N - 1) * (N - 2) // 6 - invalid
    print(f"Case #{t + 1}: {ans}")
