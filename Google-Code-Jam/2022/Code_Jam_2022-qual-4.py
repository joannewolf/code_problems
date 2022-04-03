# Chain Reactions
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000876ff1/0000000000a45ef7
# Convert the problem to tree with root as abyss, if there's only one branch then just take the max node value
# If facing multiple branches, we need to choose one as main chain and stop others at the common ancestor
# It's always better to choose the branch with min value in main chain, so we get the value of all other larger branch values

# Return tuple (max fun in main branch, sum of fun value of all side branches)
def solve(root: int):
    now = root
    curr_max = fun[now]
    while len(children[now]) == 1:
        # print("now", now)
        next = children[now][0]
        curr_max = max(curr_max, fun[next])
        now = next
    # print("now", now, "curr_max", curr_max, "# children", len(children[now]))
    if len(children[now]) == 0:
        return (curr_max, 0)
    else:
        main_fun = []
        side_fun = []
        for next in children[now]:
            (next_main, next_side) = solve(next)
            main_fun.append(next_main)
            side_fun.append(next_side)
        final_main = max(curr_max, min(main_fun))
        final_side = sum(main_fun) - min(main_fun) + sum(side_fun)
        return (final_main, final_side)

T = int(input())
for t in range(T):
    N = int(input())
    fun = [int(x) for x in input().split()]
    next = [int(x) for x in input().split()]

    fun.insert(0, 0)
    children = [list() for _ in range(N+1)]
    for i in range(N):
        children[next[i]].append(i+1)
    # print(children)

    (final_main, final_side) = solve(0)

    print(f"Case #{t + 1}: {final_main + final_side}")
