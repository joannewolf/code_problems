# Using queue
def BFS_iterative(root):
    node_to_check = [root]
    while node_to_check:
        current_node = node_to_check.pop(0)
        print(current_node)
        for child in children[current_node]:
            node_to_check.append(child)

# To check if graph has cycle
def BFS_iterative2(root):
    checked = [False] * N
    node_to_check = [root]
    while node_to_check:
        current_node = node_to_check.pop(0)
        checked[current_node] = True
        print(current_node)
        for child in children[current_node]:
            if checked[child]:
                # Not revisit checked child to prevent infinite loop
                has_cycle = True
            else:
                node_to_check.append(child)

# Process one level of nodes at a time
def BFS_recursive(nodes, level):
    next_nodes = []
    for node in nodes:
        next_nodes.append(children[node])
    BFS_recursive(next_nodes, level + 1)

BFS_recursive([root], 0)

# Process one node at a time
def BFS_recursive2(queue):
    current_node = queue.pop(0)
    for child in children[current_node]:
        queue.append(child)
    BFS_recursive(queue)

# To check if graph has cycle
def BFS_recursive3(node_to_check, checked):
    current_node = node_to_check.pop(0)
    checked[current_node] = True
    for child in children[current_node]:
        if checked[child]:
            # Not revisit checked child to prevent infinite loop
            has_cycle = True
        else:
            node_to_check.append(child)
    BFS_recursive(node_to_check, checked)
