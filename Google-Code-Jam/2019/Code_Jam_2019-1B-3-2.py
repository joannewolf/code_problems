# Fair Fight
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000051706/0000000000122838
# O(NlogN)
# From kamyu104's answer, https://github.com/kamyu104/GoogleCodeJam-2019/blob/master/Round%201B/fair-fight.py

def update_max_idx_stack(A, max_idx, i, keep_same=False):
    while max_idx and A[max_idx[-1]] <= A[i] - int(keep_same):
        max_idx.pop()
    max_idx.append(i)

# Since A[max_idx[]] is descending, find min element index which > target
def binary_search(A, max_idx, target):
    l = 0
    r = len(max_idx) - 1
    while l <= r:
        mid = (l + r) // 2
        if A[max_idx[mid]] <= target:
            r = mid - 1
        else:
            l = mid + 1
    return r

T = int(input())
for t in range(T):
    [N, K] = [int(n) for n in input().split()]
    C = [int(n) for n in input().split()]
    D = [int(n) for n in input().split()]

    # For each i, find # of fair intervals (L, R) which Charles chooses sword i
    # -> L <= i <= R and max(C[L], C[L+1], ..., C[R]) = C[i] and C[i] - K <= max(D[L], D[L+1], ..., D[R]) <= C[i] + K
    # -> with condition max(C[L], C[L+1], ..., C[R]) = C[i], (# max(D[L], D[L+1], ..., D[R]) - C[i] <= K) - (# max(D[L], D[L+1], ..., D[R]) - C[i] <= -K-1)
    result = 0
    C_right_max_idx = [] # descending idx stack, C[idx] is descending, meaning the local maximum from i looking rightward
                         # e.g. idx = [5, 3], max(C[i], .., C[3]) = C[3]; max(C[i], .., C[4]) = C[3]; max(C[i], .., C[5]) = C[5]
    D_right_max_idx = []
    C_left_max_idx = [] # ascending idx stack, C[idx] is descending, meaning the local maximum from i looking leftward
    D_left_max_idx = []
    D_R = []
    for i in range(N - 1, -1, -1):
        update_max_idx_stack(C, C_right_max_idx, i)
        update_max_idx_stack(D, D_right_max_idx, i)
        if D[i] - C[i] > K:
            continue
        D_R_good_it = binary_search(D, D_right_max_idx, C[i] + K)
        D_R_bad_it = binary_search(D, D_right_max_idx, C[i] - K - 1)
        D_R_good = D_right_max_idx[D_R_good_it] - 1 if D_R_good_it >= 0 else N - 1 # rightmost idx of max_D s.t. max_D-C[i] <= K
        D_R_bad = D_right_max_idx[D_R_bad_it] - 1 if D_R_bad_it >= 0 else N - 1 # rightmost idx of max_D s.t. max_D-C[i] <= -K-1
        C_R = C_right_max_idx[-2] - 1 if len(C_right_max_idx) >= 2 else N - 1  # rightmost idx of C s.t. C[i] >= C[idx] -> maintain C[i] is the max in interval
        D_R_good = min(D_R_good, C_R)
        D_R_bad = min(D_R_bad, C_R)

        D_R.append([D_R_good, D_R_bad])

    for i in range(N):
        update_max_idx_stack(C, C_left_max_idx, i, True) # keep the idx where C[idx] == Ci
        update_max_idx_stack(D, D_left_max_idx, i)

        if D[i] - C[i] > K:
            continue
        D_L_good_it = binary_search(D, D_left_max_idx, C[i] + K)
        D_L_bad_it = binary_search(D, D_left_max_idx, C[i] - K - 1)
        D_L_good = D_left_max_idx[D_L_good_it] + 1 if D_L_good_it >= 0 else 0 # leftmost idx of max_D s.t. max_D-C[i] <= K
        D_L_bad = D_left_max_idx[D_L_bad_it] + 1 if D_L_bad_it >= 0 else 0 # leftmost idx of max_D s.t. max_D-C[i] <= -K-1
        C_L = C_left_max_idx[-2] + 1 if len(C_left_max_idx) >= 2 else 0  # leftmost idx of C s.t. C[idx] < C[i] -> maintain C[i] is the max in interval
        D_L_good = max(D_L_good, C_L)
        D_L_bad = max(D_L_bad, C_L)

        [D_R_good, D_R_bad] = D_R.pop()
        # Final index should be D_L_good <= D_L_bad <= i <= D_R_bad <= D_R_good, either left or right bound needs to be between bad and good
        result += (i - D_L_good + 1) * (D_R_good - i + 1) - (i - D_L_bad + 1) * (D_R_bad - i + 1)

    print("Case #{}: {}".format(t + 1, result))
