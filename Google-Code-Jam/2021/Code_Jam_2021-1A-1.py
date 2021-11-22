# Append Sort
# https://codingcompetitions.withgoogle.com/codejam/round/000000000043585d/00000000007549e5

T = int(input())
for t in range(T):
    N = int(input())
    nums_str = input().split()

    result = 0
    for i in range(1, N):
        done = False
        for j in range(min(len(nums_str[i - 1]), len(nums_str[i]))):
            if (nums_str[i][j] > nums_str[i - 1][j]):
                add_digit = max(len(nums_str[i - 1]) - len(nums_str[i]), 0)
                result += add_digit
                nums_str[i] += '0' * add_digit
                done = True
                break
            elif (nums_str[i][j] < nums_str[i - 1][j]):
                add_digit = max(len(nums_str[i - 1]) + 1 - len(nums_str[i]), 0)
                result += add_digit
                nums_str[i] += '0' * add_digit
                done = True
                break
        if not done:
            # Xi-1 and Xi has same prefix
            if (len(nums_str[i]) < len(nums_str[i - 1])):
                if ( nums_str[i - 1][len(nums_str[i]):] == '9' * (len(nums_str[i - 1]) - len(nums_str[i])) ):
                    # Xi-1 longer, and remaining 999..., then Xi need to add 0000...
                    add_digit = len(nums_str[i - 1]) + 1 - len(nums_str[i])
                    result += add_digit
                    nums_str[i] += '0' * add_digit
                else:
                    # Xi-1 longer, then Xi need to add remain num + 1
                    add_digit = len(nums_str[i - 1]) - len(nums_str[i])
                    result += add_digit
                    remain_num = nums_str[i - 1][len(nums_str[i]):]
                    for k in range(len(remain_num) - 1, -1, -1):
                        if remain_num[k] != '9':
                            remain_num = remain_num[0:k] + chr(ord(remain_num[k]) + 1) + '0' * (len(remain_num) - 1 - k)
                            break
                    nums_str[i] += remain_num
            elif (len(nums_str[i]) == len(nums_str[i - 1])):
                result += 1
                nums_str[i] += '0'

    # print(nums_str)
    print("Case #{}: {}".format(t + 1, result))
