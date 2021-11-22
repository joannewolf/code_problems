# Truck Delivery
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435a5b/000000000077a885
# O(N*(logN [insert sorted_path] + N [create sorted_gcd] + QlogQ [get sorted_day])), TLE but correct locally on test set 1

import math

T = int(input())
for t in range(T):
    [N, Q] = [int(n) for n in input().split()]
    edges = []
    days = []
    for i in range(N - 1):
        edges.append([int(n) for n in input().split()])
    for i in range(Q):
        days.append([i] + [int(n) for n in input().split()])

    result = [-1] * Q
    path = []
    sorted_path = []
    node_stack = [1]

    # DFS to walk thu all paths
    while (edges):
        current_node = node_stack[-1]
        # print("current_node", current_node)
        leaf_node = True
        for edge in edges:
            if (edge[0] == current_node or edge[1] == current_node):
                next_node = edge[0] if edge[1] == current_node else edge[1]
                node_stack.append(next_node)
                path.append(edge)
                # Insert to sorted_path
                l = 0
                r = len(sorted_path) - 1
                while l <= r:
                    mid = (l + r) // 2
                    if sorted_path[mid][2] <= edge[2]:
                        l = mid + 1
                    else:
                        r = mid - 1
                sorted_path.insert(l, edge)

                # Calculate all days starting from city next_node
                # sorted_path = sorted(path, key=lambda edge: edge[2]) # [city x, city y, load limit, toll]
                sorted_gcd = [sorted_path[0][2:]] # [load limit, toll gcd]
                for i in range(1, len(sorted_path)):
                    if sorted_path[i][2] == sorted_gcd[-1][0]:
                        sorted_gcd[-1][1] = math.gcd(sorted_path[i][3], sorted_gcd[-1][1])
                    else:
                        sorted_gcd.append([sorted_path[i][2], math.gcd(sorted_path[i][3], sorted_gcd[-1][1])])
                sorted_day = sorted(filter(lambda day: day[1] == next_node, days), key=lambda day: day[2], reverse=True) # [index, city, weight]
                flag = len(sorted_gcd) - 1
                for day in sorted_day:
                    while (day[2] < sorted_gcd[flag][0] and flag >= 0):
                        flag -= 1
                    if flag == -1:
                        result[day[0]] = 0
                    else:
                        result[day[0]] = sorted_gcd[flag][1]
                # print(sorted_path)
                # print(sorted_gcd)
                # print(sorted_day)
                # print()

                leaf_node = False
                edges.remove(edge)
                break
        if leaf_node:
            node_stack.pop()
            sorted_path.remove(path[-1])
            path.pop()

    print(f"Case #{t + 1}: {' '.join([str(n) for n in result])} ")
