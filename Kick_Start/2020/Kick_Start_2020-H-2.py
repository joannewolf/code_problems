# Boring Numbers
# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff49/000000000043b0c6

# Get # of boring number from pow(10, n-1) to num, inclusive
def get_count(num: str):
    ans = 0
    n = len(num)
    all_digit_pass = True
    for i in range(n):
        if i % 2 == 0: # odd digit
            ans += int(num[i]) // 2 * pow(5, n - i - 1)
            if num[i] not in '13579':
                all_digit_pass = False
                break
        else: # even digit
            ans += (int(num[i]) + 1) // 2 * pow(5, n - i - 1)
            if num[i] not in '02468':
                all_digit_pass = False
                break
    return (ans + all_digit_pass)

T = int(input())
for t in range(T):
    [L, R] = input().split()

    ans = 0
    if int(L) == pow(10, len(L) - 1):
        for i in range(len(L), len(R)):
            ans += pow(5, i)
        ans += get_count(R)
    elif len(L) == len(R):
        ans = get_count(R) - get_count(str(int(L) - 1))
    else:
        ans += get_count('9' * len(L)) - get_count(str(int(L) - 1))
        for i in range(len(L) + 1, len(R)):
            ans += pow(5, i)
        ans += get_count(R)

    print(f"Case #{t + 1}: {ans}")
