# Milk Tea
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000008f4332/0000000000943934
# Brute-force, O(PN + P*2^P), TLE on test set 2

INT_MAX = pow(2, 10) + 1

T = int(input())
for t in range(T):
    [N, M, P] = map(int, input().split())
    preferences = []
    for _ in range(N):
        preferences.append(input())
    forbidden = set()
    for _ in range(M):
        forbidden.add(input())

    bit0_count = [0] * P
    bit1_count = [0] * P
    for i in range(N):
        for j in range(P):
            if preferences[i][j] == '0':
                bit0_count[j] += 1
            else:
                bit1_count[j] += 1
    # print(bit0_count)
    # print(bit1_count)
    
    ans = INT_MAX
    for n in range(pow(2, P)):
        num = n
        count = 0
        bits = ""
        for i in range(P):
            if num % 2 == 0:
                count += bit1_count[i]
                bits += "0"
            else:
                count += bit0_count[i]
                bits += "1"
            num //= 2
        # print(n, bits, count)
        if bits not in forbidden and count < ans:
            ans = count

    print(f"Case #{t + 1}: {ans}")
