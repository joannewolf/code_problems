# Cryptopangrams
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000051705/000000000008830b
# Edge case
# 1
# 107 29
# 15 15 15 15 21 49 77 143 221 323 437 667 899 1147 1517 1763 2021 2491 3127 3599 4087 4757 5183 5767 6557 7387 8633 9797 10403
# Case #1: ABABACCDEFGHIJKLMNOPQRSTUVWXYZ

def gcd (a, b):
    while b:
        a, b = b, a % b
    return a

T = input()
for t in range(int(T)):
    [N, L] = [int(n) for n in input().split()]
    ciphertext = [int(n) for n in input().split()]
    number = []
    result = ""

    # find common prime from first two different ciphertext
    for i in range(L):
        if (ciphertext[i] != ciphertext[i + 1]):
            temp = gcd(ciphertext[i], ciphertext[i + 1])
            # print(i, temp)
            number.append(temp)
            for j in range(i + 1):
                number.insert(0, ciphertext[i] // number[0])
            break
    # find remain prime sequence
    for n in ciphertext[i + 1:]:
        if (n % number[-1] == 0):
            number.append(n // number[-1])
    # print(number)

    # build result string
    prime_list = sorted(list(set(number)))
    # print(prime_list)
    prime_dict = {}
    for i in range(26):
        prime_dict[prime_list[i]] = chr(ord('A') + i)
    # print(prime_dict)
    for n in number:
        result += prime_dict[n]

    print("Case #{}: {}".format(t + 1, result))
