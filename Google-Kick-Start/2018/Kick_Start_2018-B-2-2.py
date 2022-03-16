# Sherlock and the Bit Strings
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050ff4/000000000005107b
# Key idea: count the # of valid string given prefix and the input constraints
# Then we can fill the bits one by one (choose bit 0 first), if the prefix count >= P, then final result is within it, otherwise choose bit 1
# To get all the prefix count, use DP, define dp[i][j], i = 1~N, j = 0~2^16, means
#   The prefix is fixed until i-th bit, no matter what i - 16 bit and before are
#   The last 16 bits are as j (cuz constraints B - A >= 15, at most 16 bits)
#   This assignment satisfys all constraints where B >= i
# O(2^16 * N * K)

MAX_P = pow(10, 18) + 1
MASK = (1 << 16) - 1 # 1111111111111111, 16 1's, for taking only last 16 bits
M = (1 << 16)
one_count = [0] * M
for i in range(M):
    one_count[i] = one_count[i >> 1] + (i & 1)
    
def pass_constraints(bits: int, b: int):
    for (n, c) in constraints[b]:
        # Take only last n bits and count how many 1's
        if one_count[bits & ((1 << n) - 1)] != c:
            return False
    return True

T = int(input())
for t in range(T):
    [N, K, P] = [int(x) for x in input().split()]
    constraints = [[] for _ in range(N)]
    for _ in range(K):
        [a, b, c] = [int(x) for x in input().split()]
        constraints[b - 1].append((b - a + 1, c))

    dp = [[0] * M for _ in range(N)]
    for last_bits in range(M):
        if pass_constraints(last_bits, N - 1):
            dp[N - 1][last_bits] = 1
    for i in range(N - 2, -1, -1):
        for last_bits in range(M):
            if pass_constraints(last_bits, i):
                next = (last_bits << 1) & MASK
                dp[i][last_bits] = min(dp[i+1][next] + dp[i+1][next|1], MAX_P)

    ans = ""
    last_bits = 0
    for i in range(N):
        # Append 0 as last bit, and ignore the first bit by applying mask
        next = (last_bits << 1) & MASK
        if P <= dp[i][next]: # If choose 0 as next bit have more than P results
            ans += "0"
            last_bits = next
            # print(next, dp[i][next], "0")
        else:
            ans += "1"
            P -= dp[i][next]
            last_bits = next | 1 # Set last bit as 1
            # print(next, dp[i][next], "1")

    print(f"Case #{t + 1}: {ans}")
