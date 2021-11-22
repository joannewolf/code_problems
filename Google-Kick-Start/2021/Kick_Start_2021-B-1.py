# Increasing Substring
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435a5b/000000000077a882

T = int(input())
for t in range(T):
    N = int(input())
    S = input()

    increasing_str_len = []
    temp_len = 1
    for (i) in range(1, N):
        if (ord(S[i]) <= ord(S[i - 1])):
            increasing_str_len.append(temp_len)
            temp_len = 1
        else:
            temp_len += 1
    increasing_str_len.append(temp_len)
    # print(increasing_str_len)

    result = []
    for len in increasing_str_len:
        result.extend(list(range(1, len + 1)))

    print("Case #{}: {}".format(t + 1, ' '.join([str(n) for n in result])))
