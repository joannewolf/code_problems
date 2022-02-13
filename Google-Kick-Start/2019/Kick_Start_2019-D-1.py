# X or What?
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000051061/0000000000161426
# odd_bit XOR odd_bit = even_bit
# odd_bit XOR even_bit = odd_bit
# even_bit XOR even_bit = even_bit
# So the problem can be transform to:
# If there are even number of odd_bit, whole array is xor-even; else, it will be the subinterval without first or last odd_bit
# If using ordered data structure, O((N+Q)logN)

def is_odd_bit(num: int):
    count = 0
    while num != 0:
        count += num % 2
        num >>= 1
    return bool(count % 2)

T = int(input())
for t in range(T):
    [N, Q] = [int(n) for n in input().split()]
    nums = [int(n) for n in input().split()]
    odd_bit = set()
    for i, num in enumerate(nums):
        if is_odd_bit(num):
            odd_bit.add(i)

    ans = []
    for i in range(Q):
        [p, v] = [int(n) for n in input().split()]
        if is_odd_bit(v):
            odd_bit.add(p)
        else:
            odd_bit.discard(p)

        if len(odd_bit) % 2 == 1:
            ans.append( max(0, N - min(odd_bit) - 1, max(odd_bit)) )
        else:
            ans.append(N)

    print(f"Case #{t + 1}: {' '.join([str(n) for n in ans])}")
