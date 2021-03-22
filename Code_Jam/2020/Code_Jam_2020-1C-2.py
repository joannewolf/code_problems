# Overrandomized
# https://codingcompetitions.withgoogle.com/codejam/round/000000000019fef4/00000000003179a1

T = int(raw_input())
for t in xrange(T):
    U = int(raw_input())
    requests = []
    for i in range(10000):
        Q, R = raw_input().split(' ')
        requests.append((Q, R))
    requests.sort(key=lambda x: x[0])

    # for known M cases
    # letter_set = set()
    # letters = {} # letter -> the maximum possible digit for letter, and this letter is not 0
    # ans = ['*'] * 10
    # for query, string in requests:
    #     letter_set.update(string)
    #     if int(query) != -1 and len(query) == len(string):
    #         if (string[0] not in letters) or (string[0] in letters and int(query[0]) < letters[string[0]]):
    #             letters[string[0]] = int(query[0])
    # ans[0] = list(letter_set - set(letters.keys()))[0]
    # for letter, index in letters.items():
    #     ans[index] = letter
    # print "Case #{}: {}".format(t + 1, ''.join(ans))

    # for unknown M cases
    # the probability for getting N_i = x is 10^-16 / y for y = x...10^16-1 ~= 10^-16(ln 10^16 - ln x)
    # means when x is bigger, it's probability is smaller => leading digit are more likely smaller than larger
    # https://en.wikipedia.org/wiki/Benford%27s_law
    letter_set = set()
    letters = {} # letter -> count of being leading digit
    for _, string in requests:
        letter_set.update(string)
        if string[0] not in letters:
            letters[string[0]] = 1
        else:
            letters[string[0]] += 1
    digit0 = list(letter_set - set(letters.keys()))[0]
    ans = sorted(letters.items(), key=lambda letter: letter[1], reverse=True)
    ans = [digit0] + [a[0] for a in ans]

    print "Case #{}: {}".format(t + 1, ''.join(ans))
