# Roaring Years
# https://codingcompetitions.withgoogle.com/codejam/round/00000000004362d7/00000000007c0f01

MAX_DIGIT = 19

# roaring year can only be n * i digits or n * i + m * (i+1) digits
# the second cases are limited so calculate first
roaring_nums_with_carry = [[] for i in range(0, MAX_DIGIT + 1)]
for digit_num in range(3, MAX_DIGIT + 1):
    for i in range(1, digit_num):
        for n in range(1, digit_num // i):
            # if digit_num == n * i + m * (i+1) digits
            if (digit_num - n * i) % (i + 1) == 0:
                base = pow(10, i)
                m = (digit_num - n * i) // (i + 1)
                if base - n > 0:
                    roaring_nums_with_carry[digit_num].append( "".join([str(x) for x in range(base - n, base + m)]) )
# for arr in roaring_nums_with_carry:
#     print(arr)

# min_roaring_num[i]: the min roaring num with i digits
min_roaring_num = [""] * (MAX_DIGIT + 2)
for i in range(2, MAX_DIGIT + 2):
    for j in range(i // 2, 0, -1):
        if i % j == 0:
            if j != 1:
                base = pow(10, j - 1)
                min_roaring_num[i] = "".join([str(x) for x in range(base, base + i // j)])
            else:
                if i < 10:
                    min_roaring_num[i] = "".join([str(x) for x in range(1, i + 1)])
                else:
                    min_roaring_num[i] = "".join([str(x) for x in range(1, 10 + (i - 9) // 2)])
            break
# print(min_roaring_num)

T = int(input())
for t in range(T):
    Y = input()
    digit_num = len(Y)

    candidates = []
    for i in range(digit_num // 2, 0, -1):
        # if digit_num == n * i digits
        if digit_num % i == 0:
            base = int(Y[0:i])
            candidates.append("".join([str(x) for x in range(base, base + digit_num // i)]))
            candidates.append("".join([str(x) for x in range(base + 1, base + digit_num // i + 1)]))
    candidates += roaring_nums_with_carry[digit_num]
    candidates.append(min_roaring_num[digit_num + 1])

    candidates = [int(x) for x in candidates]
    candidates.sort()
    # print(candidates)
    for candidate in candidates:
        if candidate > int(Y):
            print("Case #{}: {}".format(t + 1, candidate))
            break
