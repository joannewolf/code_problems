# Bundling
# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ffc7/00000000001d3ff3

def get_prefix(str1, str2):
    flag = 0
    while flag < len(str1) and flag < len(str2):
        if str1[flag] == str2[flag]:
            flag += 1
        else:
            break
    return str1[0:flag]

T = int(input())
for t in range(T):
    [N, K] = [int(n) for n in input().split()]
    strings = []
    for i in range(N):
        strings.append(input())
    strings.sort()

    prefix_len = set()
    prefix = []
    current = get_prefix(strings[0], strings[1])
    count = 1
    for i in range(2, N):
        temp = get_prefix(strings[i-1], strings[i])
        if temp != current:
            prefix.append([current, count])
            prefix_len.add(len(current))
            current = temp
            count = 1
        else:
            count += 1
    prefix_len.add(len(current))
    prefix.append([current, count])
    # print(prefix)
    # print(prefix_len)

    ans = 0
    prefix_len = sorted(list(prefix_len), reverse=True) # Process long prefix first
    prefix_len_flag = 0
    while prefix:
        prefix_flag = 0
        current_len = prefix_len[prefix_len_flag]
        # print("current_len", current_len)
        while prefix_flag < len(prefix):
            if len(prefix[prefix_flag][0]) == current_len:
                group = (prefix[prefix_flag][1] + 1) // K
                ans += group * current_len
                # print(prefix_flag, prefix[prefix_flag][0], group)

                extra = (prefix[prefix_flag][1] + 1) % K - 1
                if len(prefix) == 1:
                    prefix.pop(prefix_flag)
                    break
                elif prefix_flag == 0:
                # Merge current extra prefix to right
                    prefix[1][1] += extra
                    if prefix[1][1] == 0:
                        prefix.pop(1)
                    prefix.pop(0)
                elif prefix_flag == len(prefix) - 1:
                # Merge current extra prefix to left
                    prefix[-2][1] += extra
                    if prefix[-2][1] == 0:
                        prefix.pop(-2)
                    prefix.pop(-1)
                elif len(prefix[prefix_flag - 1][0]) < len(prefix[prefix_flag + 1][0]):
                # Merge current extra prefix to right
                    prefix[prefix_flag + 1][1] += extra
                    if prefix[prefix_flag + 1][1] == 0:
                        prefix.pop(prefix_flag + 1)
                    prefix.pop(prefix_flag)
                elif len(prefix[prefix_flag - 1][0]) > len(prefix[prefix_flag + 1][0]):
                # Merge current extra prefix to left
                    prefix[prefix_flag - 1][1] += extra
                    prefix.pop(prefix_flag)
                    if prefix[prefix_flag - 1][1] == 0:
                        prefix.pop(prefix_flag - 1)
                else:
                # Left and right prefix are same, merge left, current extra, right together
                    prefix[prefix_flag - 1][1] += extra
                    prefix[prefix_flag - 1][1] += prefix[prefix_flag + 1][1]
                    prefix.pop(prefix_flag)
                    prefix.pop(prefix_flag)
                # print(prefix)
            else:
                prefix_flag += 1
        prefix_len_flag += 1

    print(f"Case #{t + 1}: {ans}")
