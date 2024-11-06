# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(P, Q):
    # Implement your solution here
    pairs = list(zip(P, Q))
    for i, pair in enumerate(pairs):
        pairs[i] = tuple(sorted(pair))
    pairs = set(pairs) # distinct char pairs

    result = 0
    mask = 0 # bit 0~25 record whether 'a'~'z' has appeared
    diff_pairs = []
    for i, j in pairs:
        if i == j: # same char in P and Q have no choice
            result += 1
            mask += 1 << (ord(i) - ord('a'))
        else:
            diff_pairs.append((ord(i) - ord('a'), ord(j) - ord('a')))

    # recursively try all pairs of diff char
    def backtrack(i, mask):
        if i == len(diff_pairs):
            return 0
        
        j, k = diff_pairs[i]
        if (mask >> j) & 1 or (mask >> k) & 1: # if one of the char has appeared
            # greedily use the char appeared and continue
            return backtrack(i+1, mask)

        # neither char in pair appeared, so choose either one and compare
        return 1 + min(backtrack(i + 1, mask + (1 << j)), backtrack(i + 1, mask+(1 << k)))

    return result + backtrack(0, mask)
