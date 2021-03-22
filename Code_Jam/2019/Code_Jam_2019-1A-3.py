# Alien Rhyme
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000051635/0000000000104e05
# Edge case
# 1
# 8
# COAJAM
# COBJAM
# COCJAM
# CODJAM
# COEJAM
# COFJAM
# COGJAM
# Case #1: 6

# find longest common prefix not in ryhme_set
def find_new_lcp(str1, str2, ryhme_set):
    result = ""
    for i in range(min(len(str1), len(str2))):
        if (str1[i] == str2[i] and result + str1[i] not in ryhme_set):
            result += str1[i]
        else:
            break
    return result

T = input()
for t in range(int(T)):
    N = int(input())
    words = []
    # reverse words and sort, so the problem becomes dealing with prefix
    for i in range(N):
        words.append(input()[::-1])
    words.sort()
    # print(words)

    ryhme_set = set()
    while True:
        new_added = False
        max_prefix_len = 0
        max_prefix_index = -1
        # find next new longest rhyme
        for i in range(len(words) - 1):
            temp_prefix = find_new_lcp(words[i], words[i + 1], ryhme_set)
            if (len(temp_prefix) > max_prefix_len):
                max_prefix_len = len(temp_prefix)
                max_prefix_index = i
                max_prefix = temp_prefix
        # print(max_prefix_len, max_prefix_index, max_prefix)
        if max_prefix_index != -1:
            ryhme_set.add(max_prefix)
            del words[max_prefix_index]
            del words[max_prefix_index]
        else:
            break

    print("Case #{}: {}".format(t + 1, len(ryhme_set) * 2))
