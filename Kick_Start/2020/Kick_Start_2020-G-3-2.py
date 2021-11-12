# Combination Lock
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000001a0069/0000000000414a24
# Sort initial values, and for each Xi find index 1 <= p <= i and i <= b <= W, such that distance can be calculated as below
# 1---------p-------i-------b---------W
#   N-Xi+Xr   Xi-Xq   Xc-Xi   N-Xd+Xi
# Xp = Xi - N / 2, Xb = Xi + N / 2
# p and b can be found in O(logW) using binary search, and sum(distance to Xi) can be found in O(1) with prefix sum array
# O(WlogW)

# Sum of subarray X[l] ~ X[r], inclusive
def get_sum(l, r):
    if l <= r:
        if l <= 0:
            return prefix_sum[r]
        else:
            return prefix_sum[r] - prefix_sum[l - 1]
    else:
        return 0

INF = pow(10, 14)
T = int(input())
for t in range(T):
    [W, N] = [int(n) for n in input().split()]
    X = [int(n) for n in input().split()]
    X.sort()
    prefix_sum = [X[0]]
    for i in range(1, W):
        prefix_sum.append(prefix_sum[-1] + X[i])
    # print(prefix_sum)

    ans = INF
    for i in range(W):
        sum = 0
        # Find the min index which Xi - X* > N - Xi + X*
        l, r = 0, i
        while l <= r:
            mid = (l + r) // 2
            diff = X[i] - X[mid]
            if diff > N - diff:
                l = mid + 1
            else:
                r = mid - 1
        # print("l", l, "r", r)
        # index l ~ i use Xi-X
        sum += (i - l + 1) * X[i] - get_sum(l, i)
        # index 0 ~ l - 1 use N-Xi+X, 
        sum += l * (N - X[i]) + get_sum(0, l - 1)

        # Find the max index which X* - Xi > N - X* + Xi
        l, r = i, W - 1
        while l <= r:
            mid = (l + r) // 2
            diff = X[mid] - X[i]
            if diff > N - diff:
                r = mid - 1
            else:
                l = mid + 1
        # print("l", l, "r", r)
        # index i ~ r use X-Xi
        sum += get_sum(i, r) - (r - i + 1) * X[i]
        # index r + 1 ~ W - 1 use N-X+Xi, 
        sum += (W - r - 1) * (N + X[i]) - get_sum(r + 1, W - 1)

        ans = min(ans, sum)

    print(f"Case #{t + 1}: {ans}")
