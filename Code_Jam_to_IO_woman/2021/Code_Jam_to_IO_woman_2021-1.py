# Impartial Offerings
# https://codingcompetitions.withgoogle.com/codejamio/round/00000000004360f2/0000000000777098

T = int(input())
for t in range(T):
    N = int(input())
    S = [int(n) for n in input().split()]

    animals = {}
    for s in S:
        if s not in animals:
            animals[s] = 1
        else:
            animals[s] += 1
    animals = sorted([(k, v) for k, v in animals.items()])
    # print(animals)

    result = 0
    for i, animal in enumerate(animals):
        result += (i + 1) * animal[1]

    print(f"Case #{t + 1}: {result}")
