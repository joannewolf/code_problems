# The Equation
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050e02/000000000018fe36

n_bits = 50 # Max A_i <= 10^15, log2(10^15) = 49.xx, so 50 bits can cover all numbers
T = int(input())
for t in range(T):
    [N, M] = [int(x) for x in input().split()]
    nums = [int(x) for x in input().split()]
    # for num in nums:
    #     print(f"{num:#010b}")

    bits_0 = [0] * n_bits
    for i in range(n_bits):
        for j in range(N):
            if nums[j] % 2 == 0:
                bits_0[i] += 1
            nums[j] //= 2
    # print(bits_0)

    min_sum = [0]
    for i in range(n_bits):
        # If # 0 bits < # 1 bits, choose 1 as K's i-th bit will give smaller sum
        if bits_0[i] < N - bits_0[i]:
            min_sum.append(min_sum[-1] + pow(2, i) * bits_0[i])
        else:
            min_sum.append(min_sum[-1] + pow(2, i) * (N - bits_0[i]))
    min_sum.pop(0)
    # print(min_sum)

    k = []
    for i in range(n_bits-1, -1, -1):
        if (i == 0 and pow(2, i) * bits_0[i] <= M) or (pow(2, i) * bits_0[i] + min_sum[i - 1] <= M):
        # Choose bit 1 for k's i-th bit, greedily choose 1 first to make larger k
            k.append(1)
            M -= pow(2, i) * bits_0[i]
        elif (i == 0 and pow(2, i) * (N - bits_0[i]) <= M) or (pow(2, i) * (N - bits_0[i]) + min_sum[i - 1] <= M):
        # Choose bit 0 for k's i-th bit
            k.append(0)
            M -= pow(2, i) * (N - bits_0[i])
        else:
            break
    # print(len(k))
    # print(k)

    if len(k) < n_bits:
        ans = -1
    else:
        ans = 0
        for i in range(n_bits):
            ans = ans * 2 + k[i]

    print(f"Case #{t + 1}: {ans}")
