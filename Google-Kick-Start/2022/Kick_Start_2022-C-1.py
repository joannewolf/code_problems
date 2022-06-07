# New Password
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000008cb4d1/0000000000b20f15

lower_case = 'abcdefghijklmnopqrstuvwxyz'
upper_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digit = '0123456789'
special_char = '#@*&'

T = int(input())
for t in range(T):
    N = int(input())
    password = input()

    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    for c in upper_case:
        if c in password:
            has_upper = True
            break
    for c in lower_case:
        if c in password:
            has_lower = True
            break
    for c in digit:
        if c in password:
            has_digit = True
            break
    for c in special_char:
        if c in password:
            has_special = True
            break

    if not has_upper:
        password += 'A'
        N += 1
    if not has_lower:
        password += 'a'
        N += 1
    if not has_digit:
        password += '1'
        N += 1
    if not has_special:
        password += '#'
        N += 1
    if N < 7:
        password += 'A' * (7 - N)

    print(f"Case #{t + 1}: {password}")
