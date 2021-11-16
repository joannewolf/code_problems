# Transform the String
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435914/00000000008da461

T = int(input())
for t in range(T):
    S = input()
    F = input()

    ans = 0
    for c in S:
        min_dist = 30
        for letter in F:
            dist = abs(ord(c) - ord(letter))
            min_dist = min(min_dist, dist, 26 - dist)
        ans += min_dist
    print(f"Case #{t + 1}: {ans}")
