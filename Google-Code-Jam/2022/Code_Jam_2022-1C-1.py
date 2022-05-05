# Letter Blocks
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000877b42/0000000000afe6a1

ascii_A = ord('A')

T = int(input())
for t in range(T):
    N = int(input())
    S = input().split()

    impossible = False
    contiguous = [0] * 26
    start = [-1] * 26 # start[i] = j, i.e. S[j][0] - ascii_A = i
    end = [-1] * 26

    for i, s in enumerate(S):
        # Some substring like "ABA"
        checked = set()
        now = s[0]
        for c in s:
            if c != now and c in checked:
                impossible = True
                break
            now = c
            checked.add(c)
        if impossible:
            break

        if s[0] == s[-1]:
            contiguous[ord(s[0]) - ascii_A] += len(s)
        else:
            if start[ord(s[0]) - ascii_A] != -1 or end[ord(s[-1]) - ascii_A] != -1:
                impossible = True
                break
            start[ord(s[0]) - ascii_A] = i
            end[ord(s[-1]) - ascii_A] = i
    # print(contiguous)
    # print(start)
    # print(end)

    ans = ""
    used = set()
    if not impossible:
        for delta in range(26):
            # Start a new chain
            if start[delta] != -1 and end[delta] == -1:
                flag = start[delta]
                if S[flag][0] in used:
                    impossible = True
                    break
                else:
                    used.add(S[flag][0])

                while flag != -1:
                    letter = set(S[flag])
                    letter.remove(S[flag][0])
                    # print(flag, S[flag], letter)
                    for c in letter:
                        if c in used:
                            impossible = True
                            break
                        else:
                            used.add(c)
                    if impossible:
                        break
                    first_letter = ord(S[flag][0]) - ascii_A
                    last_letter = ord(S[flag][-1]) - ascii_A
                    ans += S[flag][0] * contiguous[first_letter] + S[flag]
                    contiguous[first_letter] = 0
                    start[first_letter] = -1
                    # print("next", last_letter)
                    flag = start[last_letter]
                if ans:
                    last_letter = ord(ans[-1]) - ascii_A
                    ans += ans[-1] * contiguous[last_letter]
                    contiguous[last_letter] = 0
            if impossible:
                break

    if not impossible:
        for delta in range(26):
            # Some strings produce loop, e.g. "AB BA"
            if start[delta] != -1:
                impossible = True
                break
        
    if not impossible:
        for delta in range(26):
            if contiguous[delta] != 0:
                if chr(ascii_A + delta) in used:
                    impossible = True
                    break
                ans += chr(ascii_A + delta) * contiguous[delta]

    if impossible:
        print(f"Case #{t + 1}: IMPOSSIBLE")
    else:
        print(f"Case #{t + 1}: {ans}")
