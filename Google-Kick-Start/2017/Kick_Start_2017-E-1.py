# Trapezoid Counting
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000201bfe/0000000000201d24

T = int(input())
for t in range(T):
    N = int(input())
    nums = [int(x) for x in input().split()]
    sticks = {}

    for i in nums:
        if i in sticks:
            sticks[i] += 1
        else:
            sticks[i] = 1
    sticks = list(sticks.items())
    sticks.sort()
    # print(sticks)

    N = len(sticks)
    prefix = [0]
    for i in range(N):
        prefix.append(prefix[-1] + sticks[i][1])
    # print(prefix)

    ans = 0
    flag3 = 0
    for i in range(N):
        # Use 2 sticks of same length, the other 2 sticks have to be different length
        # len(longer_stick) - len(shorter_stick) < 2 * stick[i], otherwise it cannot form a quadrilateral
        if sticks[i][1] >= 2:
            flag2 = 0
            candidate = 0 # The number of third, fourth edges combination candidates
            for j in range(N): # Iterate shorter stick
                if j == i:
                    continue
                while flag2 < N:
                    if sticks[flag2][0] - sticks[j][0] < 2 * sticks[i][0]:
                        flag2 += 1
                    else:
                        break
                longer = prefix[flag2] - prefix[j+1]
                if j < i and i < flag2:
                    longer -= sticks[i][1]
                candidate += longer * sticks[j][1]
            ans += sticks[i][1] * (sticks[i][1] - 1) // 2 * candidate

        # Use 3 sticks of same length, only fourth stick is different length
        # len(fourth_stick) < 3 * stick[i], otherwise it cannot form a quadrilateral
        if sticks[i][1] >= 3:
            while flag3 < N:
                if sticks[flag3][0] < 3 * sticks[i][0]:
                    flag3 += 1
                else:
                    break
            candidate = prefix[flag3] - sticks[i][1] # The number of fourth edge candidates
            ans += sticks[i][1] * (sticks[i][1] - 1) * (sticks[i][1] - 2) // 6 * candidate

    print(f"Case #{t + 1}: {ans}")
