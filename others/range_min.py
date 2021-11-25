# Range minimum query https://en.wikipedia.org/wiki/Range_minimum_query
# Given a array, return the min/max value of subarray [l, r]

import math

# Sparse table
# Can only handle static array
# Pre-processing O(NlogN), query O(1)
array = [1, 5, 8, 2, 3, 6, 4]
N = len(array)
K = math.floor(math.log2(N))
sparse = [[0] * (K+1) for i in range(N)]
# sparse[i][k]: the min/max value of subarray starting from array[i] with length 2^k
for i in range(N):
    sparse[i][0] = array[i]
for k in range(1, K+1):
    for i in range(N - pow(2, k-1)):
        # Every 2^k subarray can be combined by 2 2^(k-1) subarray
        sparse[i][k] = min(sparse[i][k-1], sparse[i + pow(2, k-1)][k-1])

# Range [l, r] can be covered by 2 floor(log2(r - l + 1)) subarray
# Even though there might be overlap, but it won't affect the final min/max result
def query(l, r):
    k = math.floor(math.log2(r - l + 1))
    ans = min(sparse[l][k], sparse[r - pow(2, k) + 1][k])
    print("l", l, "r", r, "ans", ans)

print(array)
query(0, 4)
query(2, 3)
query(2, 5)
query(0, 6)
query(1, 2)
query(4, 6)

# Segment tree
# Allow modifications to the array between answering queries
# Pre-processing O(N), query O(logN), update O(logN)