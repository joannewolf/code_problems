# Longest Progression
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435a5b/000000000077a3a5

T = int(input())
for t in range(T):
    N = int(input())
    nums = [int(n) for n in input().split()]

    diffs = []
    for i in range(1, N):
        diffs.append(nums[i] - nums[i - 1])
    # merge consecutive same diffs into chunks
    diff_chunks = []
    for i in range(0, N - 1):
        if (not diff_chunks or diffs[i] != diff_chunks[-1][0]):
            diff_chunks.append([diffs[i], 1])
        else:
            diff_chunks[-1][1] += 1
    # print(diffs)
    # print(diff_chunks)

    result = 0
    for i in range(0, len(diff_chunks)):
        # use diff_chunks[i] as the common diff
        # if fix number after, get longest length
        temp_len = diff_chunks[i][1] + 1
        if (i == len(diff_chunks) - 1):
            temp_len += 0
        elif (i == len(diff_chunks) - 2):
            temp_len += 1
        elif (diff_chunks[i + 1][1] != 1):
            temp_len += 1
        elif ((diff_chunks[i + 1][0] + diff_chunks[i + 2][0]) != diff_chunks[i][0] * 2):
            temp_len += 1
        elif ((diff_chunks[i + 1][0] + diff_chunks[i + 2][0]) == diff_chunks[i][0] * 2):
            temp_len += 2
            if (diff_chunks[i + 2][1] == 1 and i + 3 < len(diff_chunks) and diff_chunks[i + 3][0] == diff_chunks[i][0]):
                temp_len += diff_chunks[i + 3][1]

        if (temp_len > result):
            result = temp_len

        # if fix number before, get longest length
        temp_len = diff_chunks[i][1] + 1
        if (i == 0):
            temp_len += 0
        elif (i == 1):
            temp_len += 1
        elif (diff_chunks[i - 1][1] != 1):
            temp_len += 1
        elif ((diff_chunks[i - 1][0] + diff_chunks[i - 2][0]) != diff_chunks[i][0] * 2):
            temp_len += 1
        elif ((diff_chunks[i - 1][0] + diff_chunks[i - 2][0]) == diff_chunks[i][0] * 2):
            temp_len += 2
            if (diff_chunks[i - 2][1] == 1 and i - 3 >= 0 and diff_chunks[i - 3][0] == diff_chunks[i][0]):
                temp_len += diff_chunks[i - 3][1]

        if (temp_len > result):
            result = temp_len

    print("Case #{}: {}".format(t + 1, result))
