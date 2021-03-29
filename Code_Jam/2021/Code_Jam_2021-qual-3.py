# Reversort Engineering
# https://codingcompetitions.withgoogle.com/codejam/round/000000000043580a/00000000006d12d7

T = input()
for t in range(int(T)):
    [N, C] = [int(n) for n in input().split()]

    if (C < N - 1 or C > (2 + N) * (N - 1) / 2):
        print("Case #{}: IMPOSSIBLE".format(t + 1))
    else:
        # create a reverse plan
        plan = [1] * (N - 1)
        C -= (N - 1)
        for i in range(N - 1):
            if (C == 0):
                break
            elif (C > N - i - 1):
                plan[i] += N - i - 1
                C -= (N - i - 1)
            else:
                plan[i] += C
                C -= C
        # print(plan)

        index = list(range(0, N))
        # perform Reversort based on plan
        for i in range(N - 1):
            index[i : i + plan[i]] = index[i : i + plan[i]][::-1]

        nums = ['x'] * N
        for i in range(N):
            nums[index[i]] = str(i + 1)
        print("Case #{}: {}".format(t + 1, ' '.join(nums)))
