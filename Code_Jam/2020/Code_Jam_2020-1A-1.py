# Pattern Matching
# https://codingcompetitions.withgoogle.com/codejam/round/000000000019fd74/00000000002b3034

T = int(raw_input())
for t in xrange(T):
    N = int(raw_input())
    patterns = []
    for n in xrange(N):
        patterns.append(raw_input())

    prefix = sorted([s[0: s.find("*")] for s in patterns])
    prefix = filter(lambda s: s, prefix)
    suffix = sorted([s[s.rfind("*") + 1: ] for s in patterns])
    suffix = filter(lambda s: s, suffix)
    middle = [s[s.find("*") + 1: s.rfind("*")].replace("*", "") for s in patterns]

    longest_prefix = "" if not prefix else max(prefix, key = len)
    longest_suffix = "" if not suffix else max(suffix, key = len) 

    ans = ""
    for temp_prefix in prefix:
        if longest_prefix[0: len(temp_prefix)] != temp_prefix:
            ans = "*"
            break
    for temp_suffix in suffix:
        if longest_suffix[-len(temp_suffix):] != temp_suffix:
            ans = "*"
            break
    if ans != "*":
        ans = longest_prefix + "".join(middle) + longest_suffix

    print "Case #{}: {}".format(t + 1, ans)