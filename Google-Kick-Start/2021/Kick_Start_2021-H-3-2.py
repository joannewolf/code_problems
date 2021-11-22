# Silly Substitutions
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435914/00000000008d94f5
# Make each number as linked-list node, while doing replace, instead of checking whole string, we only check those "interested pointer" set
# Each conversion will take O(1) to update linked-list, overall O(N)

class ListNode:
  def __init__(self, data: int): 
    self.data = data
    self.prev = None
    self.next = None
    return

T = int(input())
for t in range(T):
    N = int(input())
    S = input()
    nodes = []
    interested = [set() for _ in range(10)] # interested[i]: The node which has data i and next node has data (i + 1) % 10

    for i, num in enumerate(S):
        node = ListNode(int(num))
        nodes.append(node)
        if i != 0:
            nodes[i - 1].next = node
            node.prev = nodes[i - 1]
            if (nodes[i - 1].data + 1) % 10 == int(num):
                interested[nodes[i - 1].data].add(nodes[i - 1])

    root = nodes[0]
    while True:
        no_more_change = True
        for i in range(10):
            # Every node in interested[i] can be converted
            for node in interested[i]:
                new_node = ListNode((i + 2) % 10)
                if node.prev is not None:
                    node.prev.next = new_node
                else:
                    root = new_node
                new_node.prev = node.prev
                new_node.next = node.next.next
                if node.next.next is not None:
                    node.next.next.prev = new_node

                if node.next in interested[(i + 1) % 10]:
                    interested[(i + 1) % 10].remove(node.next)
                if new_node.prev is not None and new_node.prev.data == (i + 1) % 10:
                    interested[(i + 1) % 10].add(new_node.prev)
                if new_node.prev is not None and new_node.prev in interested[(i - 1) % 10]:
                    interested[(i - 1) % 10].remove(new_node.prev)
                if new_node.next is not None and new_node.next.data == (i + 3) % 10:
                    interested[(i + 2) % 10].add(new_node)
                no_more_change = False
            interested[i] = set()
        if no_more_change:
            break

    ans = ""
    while root is not None:
        ans += str(root.data)
        root = root.next
    print(f"Case #{t + 1}: {ans}")
