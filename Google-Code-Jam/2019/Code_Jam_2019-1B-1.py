# Manhattan Crepe Cart
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000051706/000000000012295c

T = input()
for t in range(int(T)):
    [P, Q] = [int(n) for n in input().split()]

    face_N = [0] * (Q + 1)
    face_S = [0] * (Q + 1)
    face_E = [0] * (Q + 1)
    face_W = [0] * (Q + 1)
    for i in range(P):
        [x, y, d] = input().split()
        if (d == 'N'):
            face_N[int(y)] += 1
        elif (d == 'S'):
            face_S[int(y)] += 1
        elif (d == 'E'):
            face_E[int(x)] += 1
        elif (d == 'W'):
            face_W[int(x)] += 1

    # print("face_N", face_N)
    # print("face_S", face_S)
    # print("face_E", face_E)
    # print("face_W", face_W)

    result_x = -1
    max_count_x = -1
    count_e = 0
    count_w = sum(face_W)
    for i in range(Q + 1):
        count_w -= face_W[i]
        # print("x", i, count_e + count_w)
        if (count_e + count_w > max_count_x):
            max_count_x = count_e + count_w
            result_x = i
        count_e += face_E[i]

    result_y = -1
    max_count_y = -1
    count_n = 0
    count_s = sum(face_S)
    for i in range(Q + 1):
        count_s -= face_S[i]
        # print("y", i, count_n + count_s)
        if (count_n + count_s > max_count_y):
            max_count_y = count_n + count_s
            result_y = i
        count_n += face_N[i]

    print("Case #{}: {} {}".format(t + 1, result_x, result_y))
