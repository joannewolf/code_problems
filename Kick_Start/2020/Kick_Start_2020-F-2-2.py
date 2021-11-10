# Metal Harvest
# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff48/00000000003f4b8b
# O(NlogN)

T = int(input())
for t in range(T):
    [N, K] = [int(n) for n in input().split()]
    intervals = []
    for i in range(N):
        [s, e] = [int(n) for n in input().split()]
        intervals.append((s, e))

    intervals.sort()
    ans = 0
    flag = intervals[0][0]
    i = 0
    while i < N:
        temp = (intervals[i][1] - flag) // K
        ans += temp
        if flag + temp * K == intervals[i][1]:
        # Robot stops at the end of current interval, starting next iteration from next interval's start
            i += 1
            if i != N:
                flag = intervals[i][0]
        else:
        # Robot stops in the middle of current interval, deploy robot one more time and see where it ends
            ans += 1
            while i < N and intervals[i][1] < flag + (temp + 1) * K:
                i += 1
            if i != N:
                if flag + (temp + 1) * K < intervals[i][0]:
                # If robot stops before next interval starts, starting next iteration from next interval's start
                    flag = intervals[i][0]
                else:
                # If robot stops in the middle of next interval, starting next iteration from that point
                    flag += (temp + 1) * K

    print(f"Case #{t + 1}: {ans}")
