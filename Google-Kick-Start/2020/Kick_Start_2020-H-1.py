# Retype
# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff49/000000000043adc7

T = int(input())
for t in range(T):
    [N, K, S] = [int(n) for n in input().split()]

    option1 = (K - 1) + 1 + N
    option2 = (K - 1) + (K - S) + (N - S + 1)
    print(f"Case #{t + 1}: {min(option1, option2)}")
