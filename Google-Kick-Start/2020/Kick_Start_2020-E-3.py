# Toys
# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff47/00000000003bede9
# If a set of toys can be played indefinitely, it must satisfy sum(E) - Ei >= Ri for all i => sum(E) >= Ei + Ri
# The problem is to find out, what's the minimum toys we remove and make above condition come true
# Note that for example there exists an i violate the inequation, removing other toys won't make things better, sum'(E) still < Ei + Ri, so we have to remove toy i
# But removing toy i might make thing worse, e.g. for some other j, sum(E) >= Ej + Rj, but it's possible sum'(E) < Ej + Rj after removing toy i
# In case after removing all toys we still cannot reach indefinite, we need to calculate what's the longest playing time
# The playing time = sum(E) + prefix_sum(i) while i is the first inequation violation, cuz first round is always fine, and it will stop at second round when facing first violation
# While counting second round of E, we add toy 1~N one at a time, and remove violated toys based on E+R
# Every toy will at most added to heap once and removed from heap once, O(NlogN)

import heapq

T = int(input())
for t in range(T):
    N = int(input())
    E = []
    R = []
    for i in range(N):
        [e, r] = [int(n) for n in input().split()]
        E.append(e)
        R.append(r)

    sum_E = sum(E)
    violate_order = []
    remaining_toy = []
    max_sum = 0
    max_flag = -1
    curr_sum = sum_E

    for i in range(N):
        if curr_sum > max_sum:
            max_sum = curr_sum
            max_flag = len(violate_order)
        # heapq only support min heap, so reverse the symbol to achieve max heap
        heapq.heappush(remaining_toy, (-(E[i] + R[i]), i))
        curr_sum += E[i]
        while remaining_toy:
            if sum_E < -remaining_toy[0][0]:
                index = remaining_toy[0][1]
                violate_order.append(index)
                sum_E -= E[index]
                curr_sum -= 2 * E[index]
                heapq.heappop(remaining_toy)
            else:
                break

    if sum_E > 0:
        print(f"Case #{t + 1}: {len(violate_order)} INDEFINITELY")
    else:
        print(f"Case #{t + 1}: {max_flag} {max_sum}")
