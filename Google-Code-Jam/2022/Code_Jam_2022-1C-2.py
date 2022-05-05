# Squary
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000877b42/0000000000afdf76

T = int(input())
for t in range(T):
    [N, K] = [int(x) for x in input().split()]
    nums = [int(x) for x in input().split()]

    comb = 0
    for i in range(N):
        for j in range(i + 1, N):
            comb += nums[i] * nums[j]
    add = sum(nums)

    if comb == 0: # Already squary
        print(f"Case #{t + 1}: 0")
    elif add == 0:
        print(f"Case #{t + 1}: IMPOSSIBLE")
    elif K == 1 and comb % add != 0:
        print(f"Case #{t + 1}: IMPOSSIBLE")
    elif K == 1:
        print(f"Case #{t + 1}: {-comb // add}")
    else:
        # sum([nums, n1]) = 1
        # pair([nums, n1, n2]) = pair([nums, n1]) + n2 * sum([nums, n1])
        #   = pair([nums]) + n1 * sum(nums) + n2 = 0
        n1 = 1 - add
        n2 = -(comb + add * n1)
        print(f"Case #{t + 1}: {n1} {n2}")
