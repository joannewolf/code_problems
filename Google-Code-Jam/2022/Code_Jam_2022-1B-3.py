# ASeDatAb
# https://codingcompetitions.withgoogle.com/codejam/round/000000000087711b/0000000000acd29b
# Use random to fight random! If bit 1 count == 1 ~ 4, try to get it to 00000000; else try to get it to 11111111
# Only pass test set 1

import sys
import random

nums = [[] for _ in range(9)]
MAX_TRY = 299

for num in range(256): # 2^8
    temp = num
    string = ""
    count = 0
    for i in range(8):
        if temp & 1:
            count += 1
        string += str(temp & 1)
        temp >>= 1
    nums[count].append(string[::-1])

T = int(input())
for t in range(T):
    start = random.randint(0, 255)
    print(format(start, '#010b')[2:])
    sys.stdout.flush()

    for _ in range(MAX_TRY):
        bit = int(input())
        if bit == 0:
            break
        elif bit == 8:
            print("11111111")
            sys.stdout.flush()
        elif bit == -1:
            sys.exit()
        else:
            bit = min(bit, 8 - bit)
            print(random.choice(nums[bit]))
            sys.stdout.flush()
