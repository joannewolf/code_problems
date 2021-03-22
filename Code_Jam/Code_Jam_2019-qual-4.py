# https://codingcompetitions.withgoogle.com/codejam/round/0000000000051705/00000000000881de

# Since B <= 15 < 2^4, we can use 4 test string to contruct a 4 bit number in same column
# and use 2^4 = 16 as a cycle, so it's impossible that whole cycle of bits are broken
# i.e. 0, 1, 2, ..., 15, 0, 1, 2, ..., 
# 0 1 0 1 0 1 0 1 0 1 0 1...
# 0 0 1 1 0 0 1 1 0 0 1 1...
# 0 0 0 0 1 1 1 1 0 0 0 0...
# 0 0 0 0 0 0 0 0 1 1 1 1...

import sys

T = input()
for t in range(int(T)):
    [N, B, F] = [int(n) for n in input().split()]

    test_str = [""] * 4
    respond_str = [""] * 4
    for i in range(N):
        test_str[0] += str(i % 2)
        test_str[1] += str(i // 2 % 2)
        test_str[2] += str(i // 4 % 2)
        test_str[3] += str(i // 8 % 2)
    # print(test_str)
    for i in range(4):
        print(test_str[i])
        sys.stdout.flush()
        respond_str[i] = input()

    # build N-B number by respond string
    respond_num = []
    for i in range(N - B):
        temp = 0
        temp += (ord(respond_str[0][i]) - ord('0')) * 1
        temp += (ord(respond_str[1][i]) - ord('0')) * 2
        temp += (ord(respond_str[2][i]) - ord('0')) * 4
        temp += (ord(respond_str[3][i]) - ord('0')) * 8
        respond_num.append(temp)
    # print(respond_num)

    flag = 0
    result = []
    for i in range(N):
        if (flag >= len(respond_num) or i % 16 != respond_num[flag]):
            result.append(i)
        else:
            flag += 1
    
    print(' '.join([str(i) for i in result]))
    sys.stdout.flush()
    ans = int(input())
    if (ans == 1):
        continue
    if (ans == -1):
        sys.exit(1)
