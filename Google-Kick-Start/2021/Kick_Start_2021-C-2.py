# Alien Generator
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435c44/00000000007ec1cb
# (i + 1) * (K + (K + i)) / 2 = G
# => i * (2*K + 1 + i) = 2*G - 2*K, find K such that i have integer solution
# => K = (2*G - i*(i+1)) / (2*i + 2)

T = int(input())
for t in range(T):
    G = int(input())

    # At least K = G is one solution making i = 0
    result = 1
    i = 1
    while True:
        # K cannot be 0
        if (2 * G - i * (i + 1)) % (2 * i + 2) == 0 and (2 * G - i * (i + 1)) != 0:
            result += 1
        if (2 * G - i * (i + 1)) / (2 * i + 2) < 0:
            break
        i += 1

    print(f"Case #{t + 1}: {result}")
