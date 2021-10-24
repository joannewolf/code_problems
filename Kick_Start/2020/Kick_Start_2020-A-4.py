# Bundling
# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ffc7/00000000001d3ff3
# Too many level of recursion, RE on test set 2

def make_group(level: int, strings: list):
    # print(level, strings)
    extra = 0
    score = 0

    # Group strings with same prefix level
    count = 1
    for i in range(1, len(strings)):
        if len(strings[i]) < level + 1 or len(strings[i-1]) < level + 1 or strings[i][level] != strings[i-1][level]:
            if count == 1:
                extra += 1
            else:
                (temp_score, temp_extra) = make_group(level + 1, strings[i - count: i])
                score += temp_score
                extra += temp_extra
                count = 1
        else:
            count += 1
    if count == 1:
        extra += 1
    else:
        (temp_score, temp_extra) = make_group(level + 1, strings[-count:])
        score += temp_score
        extra += temp_extra

    score += (extra // K) * level
    extra %= K
    return (score, extra)

T = int(input())
for t in range(T):
    [N, K] = [int(n) for n in input().split()]
    strings = []
    for i in range(N):
        strings.append(input())
    strings.sort()

    (ans, _) = make_group(0, strings)
    print(f"Case #{t + 1}: {ans}")
