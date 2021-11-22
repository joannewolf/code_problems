# Nesting Depth
# https://codingcompetitions.withgoogle.com/codejam/round/000000000019fd27/0000000000209a9f

T = raw_input()
for t in xrange(int(T)):
    S = raw_input()
    nums = [int(s) for s in S]
    # add 0 in the front and in the end
    nums.insert(0, 0)
    nums.append(0)

    ans = ""
    for i in xrange(1, len(nums)):
        if nums[i - 1] < nums[i]:
            ans += '(' * (nums[i] - nums[i - 1])
        elif nums[i - 1] > nums[i]:
            ans += ')' * (nums[i - 1] - nums[i])
        ans += str(nums[i])
    # remove the last 0
    ans = ans[:-1]

    print "Case #{}: {}".format(t + 1, ans)