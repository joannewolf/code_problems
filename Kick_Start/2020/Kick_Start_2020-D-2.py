# Alien Piano
# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff08/0000000000387174

T = int(input())
for t in range(T):
    K = int(input())
    note = [int(n) for n in input().split()]

    ans = 0
    direction = 0 # 1 for increasing, -1 for decreasing
    count = 1
    for i in range(1, K):
        if direction == 0:
            if note[i] > note[i - 1]:
                direction = 1
            elif note[i] < note[i - 1]:
                direction = -1
            count = 2
        elif (note[i] - note[i - 1]) * direction > 0:
            count += 1
        elif (note[i] - note[i - 1]) * direction < 0:
            ans += (count - 1) // 4
            direction = -direction
            count = 2
    ans += (count - 1) // 4

    print(f"Case #{t + 1}: {ans}")
