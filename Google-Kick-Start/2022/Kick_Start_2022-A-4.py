# Interesting Integers
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000008cb33e/00000000009e73ea
# Brute-force, O(B*len(B))

T = int(input())
for t in range(T):
    [A, B] = [int(x) for x in input().split()]

    ans = 0
    for num in range(A, B+1):
        digits = [int(x) for x in list(str(num))]
        product = 1
        sum = 0
        for n in digits:
            product *= n
            sum += n
        if product % sum == 0:
            ans += 1

    print(f"Case #{t + 1}: {ans}")
