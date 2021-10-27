# Bike Tour
# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ffc8/00000000002d82e6

T = int(input())
for t in range(T):
    N = int(input())
    H = [int(n) for n in input().split()]

    ans = 0
    for i in range(1, N - 1):
        if H[i] > H[i - 1] and H[i] > H[i + 1]:
            ans += 1
    print(f"Case #{t + 1}: {ans}")
