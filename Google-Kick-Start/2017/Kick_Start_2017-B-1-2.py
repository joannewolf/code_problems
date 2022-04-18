# Math Encoder
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000201d27/0000000000201b7b
# Different instances of same number are taken as different, e.g. nums = [1, 2, 3, 3], there will be 2 subsets of [1, 2, 3]

MOD = pow(10, 9) + 7

T = int(input())
for t in range(T):
    N = int(input())
    nums = [int(x) for x in input().split()]

    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            ans += (nums[j] - nums[i]) * pow(2, j - i - 1)
            ans %= MOD

    print(f"Case #{t + 1}: {ans}")
