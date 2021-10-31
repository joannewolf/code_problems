# Using stack
# Print from tree's root node, top down
def DFS_iterative(root):
    checked = [False] * N
    path = [root]
    while path:
        if not checked[path[-1]]:
            print(path)
        checked[path[-1]] = True

        all_children_checked = True
        # Find next non-checked child
        for child in children[path[-1]]:
            if not checked[child]:
                path.append(child)
                all_children_checked = False
                break
        if all_children_checked:
            path.pop(-1)

# Print from tree's leaf node, bottom up
def DFS_iterative2(root):
    checked = [False] * N
    path = [root]
    while path:
        all_children_checked = True
        # Find next non-checked child
        for child in children[path[-1]]:
            if not checked[child]:
                path.append(child)
                all_children_checked = False
                break
        if all_children_checked:
            print(path)
            checked[path[-1]] = True
            path.pop(-1)

# Print from tree's root node, top down
def DFS_recursive(node, path):
    print(path + [node])
    for child in children[node]:
        DFS_recursive(child, path + [node])

# Print from tree's leaf node, bottom up
def DFS_recursive2(node, path):
    for child in children[node]:
        DFS_recursive(child, path + [node])
    print(path + [node])

# To check if graph has cycle
def DFS_recursive3(node, path, checked):
    checked[node] = True
    for child in children[node]:
        if checked[child]:
            # Not revisit checked child to prevent infinite loop
            has_cycle = True
        else:
            DFS_recursive(child, path + [node], checked)
