# Challenge Nine
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000008cb33e/00000000009e7997

T = int(input())
for t in range(T):
    digits = [int(x) for x in list(input())]
    N = len(digits)

    digit_sum = 0
    for n in digits:
        digit_sum += n

    if digit_sum % 9 == 0:
        digits.insert(1, 0)
    else:
        target = 9 - (digit_sum % 9)
        for i in range(N+1):
            if i == N or digits[i] > target:
                digits.insert(i, target)
                break

    print(f"Case #{t + 1}: {''.join(map(str, digits))}")
