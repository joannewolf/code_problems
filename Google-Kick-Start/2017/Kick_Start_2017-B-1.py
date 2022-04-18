# Math Encoder
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000201d27/0000000000201b7b
# WA, but I think the problem is not clear
# Different instances of same number are taken as same, e.g. nums = [1, 2, 3, 3], there will be 1 subset of [1, 2, 3]

MOD = pow(10, 9) + 7

T = int(input())
for t in range(T):
    N = int(input())
    temp = [int(x) for x in input().split()]
    nums = [] # Distinct num in increasing order
    count = []

    temp_num = temp[0]
    temp_count = 1
    for i in range(1, N):
        if temp[i] == temp_num:
            temp_count += 1
        else:
            nums.append(temp_num)
            count.append(temp_count)
            temp_num = temp[i]
            temp_count = 1
    nums.append(temp_num)
    count.append(temp_count)
    # print(nums)
    # print(count)

    N = len(nums)
    prefix = [1] # Prefix product of (count + 1), (count + 1) means taking 0, 1, ..., count of current num
    for i in range(N):
        prefix.append(prefix[-1] * (count[i] + 1) % MOD)
    # print(prefix)

    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            # print("i", i, nums[i], count[i], "j", j, nums[j], count[j], prefix[j] // prefix[i+1])
            ans += (nums[j] - nums[i]) * count[i] * count[j] * (prefix[j] // prefix[i+1]) % MOD
            ans %= MOD

    print(f"Case #{t + 1}: {ans}")
