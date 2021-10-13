# Shuffled Anagrams
# https://codingcompetitions.withgoogle.com/kickstart/round/000000000043585c/000000000085a152

from typing import ChainMap


T = int(input())
for t in range(T):
    S = input()
    N = len(S)

    S_index = [(char, index) for (index, char) in enumerate(S)]
    sorted_S = sorted(S_index)

    # Check if any char is more than N / 2
    count = 0
    current_char = '*'
    impossible = False
    for (c, _) in sorted_S + [('*', N)]:
        if c == current_char:
            count += 1
        elif count > N // 2:
            impossible = True
            print(f"Case #{t + 1}: IMPOSSIBLE")
            break
        else:
            count = 1
            current_char = c

    # If solution exists, split the sorted char into two half and swap
    if not impossible:
        result = ['*'] * N
        index = [i for (_, i) in sorted_S]
        char = [c for (c, _) in sorted_S[N // 2:]] + [c for (c, _) in sorted_S[0: N // 2]]
        for i, c in zip(index, char):
            result[i] = c
        result = "".join(result)
        print(f"Case #{t + 1}: {result}")
