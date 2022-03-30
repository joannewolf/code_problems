# Common Anagrams
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050e07/00000000000510f2
# Prefix sum, O(L^3)

ascii_A = ord('A')

T = int(input())
for t in range(T):
    L = int(input())
    A = input()
    B = input()

    prefix_A = [[0] for _ in range(26)]
    prefix_B = [[0] for _ in range(26)]
    for i in range(L):
        for j in range(26):
            prefix_A[j].append(prefix_A[j][-1])
            prefix_B[j].append(prefix_B[j][-1])
        prefix_A[ord(A[i]) - ascii_A][-1] += 1
        prefix_B[ord(B[i]) - ascii_A][-1] += 1

    ans = 0
    for l_a in range(L):
        for r_a in range(l_a, L):
            len = r_a - l_a + 1
            for l_b in range(L - len + 1):
                anagram = True
                for i in range(26):
                    if prefix_A[i][r_a + 1] - prefix_A[i][l_a] != prefix_B[i][l_b + len] - prefix_B[i][l_b]:
                        anagram = False
                        break
                if anagram:
                    ans += 1
                    break

    print(f"Case #{t + 1}: {ans}")
