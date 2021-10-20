# Trash Bins
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435bae/0000000000887c32

def sum_from_one(n: int):
    return int((1 + n) * n / 2)

T = int(input())
for t in range(T):
    N = int(input())
    S = list(input())

    trash = []
    for index, c in enumerate(S):
        if c == '1':
            trash.append(index)
    # print(trash)

    result = 0
    result += sum_from_one(trash[0])
    for i in range(1, len(trash)):
        distance = trash[i] - trash[i - 1] - 1
        result += sum_from_one(distance // 2)
        result += sum_from_one((distance + 1) // 2)
    result += sum_from_one(N - 1 - trash[-1])

    print(f"Case #{t + 1}: {result}")
