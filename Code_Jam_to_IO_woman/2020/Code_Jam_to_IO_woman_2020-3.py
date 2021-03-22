# Interleaved Output: Part 2
# https://codingcompetitions.withgoogle.com/codejamio/round/000000000019ff03/00000000001b5cd7
# O(N^2)

ans = 0

def loop(result, IiArray, OoArray):
    if not IiArray and not OoArray:
        IOcount = 0
        for pair in result:
            if pair[0] > 0 and pair[1] > 0:
                IOcount += 1
                global ans
                ans = max(ans, IOcount)
        # print "result! ", result, IOcount
        return
    if not IiArray or not OoArray:
        return
    Ii = IiArray.pop(0)
    for Oo in OoArray:
        safeFlag = True
        for pair in result:
            # if there's a same pattern happened before and current I/i is in between
            if pair[0] * Ii > 0 and pair[1] * Oo > 0 and abs(pair[0]) < abs(Ii) and abs(Ii) < abs(pair[1]):
                safeFlag = False
                break
        if safeFlag and abs(Ii) < abs(Oo):
            tempResult = result[:] + [(Ii, Oo)]
            tempOoArray = OoArray[:]
            tempOoArray.remove(Oo)
            loop(tempResult, IiArray[:], tempOoArray)

T = raw_input()
for t in xrange(int(T)):
    S = raw_input()

    IiArray = []
    OoArray = []
    ans = 0
    for i in xrange(len(S)):
        if S[i] == 'I':
            IiArray.append(i + 1)
        elif S[i] == 'i':
            IiArray.append(-(i + 1))
        elif S[i] == 'O':
            OoArray.append(i + 1)
        elif S[i] == 'o':
            OoArray.append(-(i + 1))

    # print IiArray
    # print OoArray

    result = []
    loop(result, IiArray, OoArray)

    print "Case #{}: {}".format(t + 1, ans)