# Final Exam
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000004361e3/000000000082bffc
# O(NlogN + M*log(N + M)), TLE but correct locally on test set 2

T = int(input())
for t in range(T):
    [N, M] = [int(n) for n in input().split()]
    problems = []
    for i in range(N):
        problems.append([int(n) for n in input().split()])
    students = [int(n) for n in input().split()]
    problems.sort()

    result = []
    for s in students:
        # Use binary search to find the max interval start which <= s
        l = 0
        r = len(problems) - 1
        while l <= r:
            mid = (l + r) // 2
            if problems[mid][0] <= s:
                l = mid + 1
            else:
                r = mid - 1
        # print("l", l, "r", r)

        # All interval > s
        if r == -1:
            result.append(problems[0][0])
            if problems[0][0] == problems[0][1]:
                problems.pop(0)
            else:
                problems[0][0] += 1
        elif problems[r][0] == s:
            result.append(s)
            if problems[r][0] == problems[r][1]:
                problems.pop(r)
            else:
                problems[r][0] = s + 1
        elif problems[r][0] < s and s < problems[r][1]:
            result.append(s)
            problems.insert(r + 1, [s + 1, problems[r][1]])
            problems[r][1] = s - 1
        elif problems[r][1] == s:
            result.append(s)
            problems[r][1] = s - 1
        elif problems[r][1] < s:
            if r == len(problems) - 1 or s - problems[r][1] <= problems[r + 1][0] - s:
                result.append(problems[r][1])
                if problems[r][0] == problems[r][1]:
                    problems.pop(r)
                else:
                    problems[r][1] -= 1
            else:
                result.append(problems[r + 1][0])
                if problems[r + 1][0] == problems[r + 1][1]:
                    problems.pop(r + 1)
                else:
                    problems[r + 1][0] += 1
        # print(problems)

    print(f"Case #{t + 1}: {' '.join([str(n) for n in result])}")
