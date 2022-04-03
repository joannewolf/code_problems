# Punched Cards
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000876ff1/0000000000a4621b

T = int(input())
for t in range(T):
    [R, C] = [int(x) for x in input().split()]

    print(f"Case #{t + 1}:")
    print(".." + '-'.join(['+'] * C))
    print(".." + '.'.join(['|'] * C))
    row1 = '-'.join(['+'] * (C+1))
    row2 = '.'.join(['|'] * (C+1))
    for _ in range(R-1):
        print(row1)
        print(row2)
    print(row1)