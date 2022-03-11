# Even Digits
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050edf/00000000000510ed

odd = ['1', '3', '5', '7', '9']

T = int(input())
for t in range(T):
    num = input()
    N = len(num)

    # Find first odd digit
    first_odd = -1
    for i in range(N):
        if num[i] in odd:
            first_odd = i
            break

    if first_odd == -1:
        ans = 0
    else:
        # Find the first legal number above
        if num[first_odd] == '9':
            flag = first_odd
            while flag != 0 and num[flag - 1] == '8':
                flag -= 1
            str1 = "20" + "0" * (N - flag - 1)
            option1 = int(str1) - int(num[flag:])
        else:
            str1 = chr(ord(num[first_odd]) + 1) + "0" * (N - first_odd - 1)
            option1 = int(str1) - int(num[first_odd:])

        # Find the first legal number below
        str2 = chr(ord(num[first_odd]) - 1) + "8" * (N - first_odd - 1)
        option2 = int(num[first_odd:]) - int(str2)

        # print("str1", str1, "str2", str2)
        ans = min(option1, option2)

    print(f"Case #{t + 1}: {ans}")
