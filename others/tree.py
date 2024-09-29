import math

# segment tree
# interval tree
# binary index tree (Fenwick tree)

# heap

# interval tree https://en.wikipedia.org/wiki/Interval_tree
# segment tree https://en.wikipedia.org/wiki/Segment_tree
# binary search tree
# treeset

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# LCA (Lowest Common Ancester)
# O(N), by recursion
def LCA_1(root: TreeNode, p: TreeNode, q: TreeNode):
    if not root or root == p or root == q:
        return root

    left = LCA_1(root.left, p, q)
    right = LCA_1(root.right, p, q)
    if not left and not right:
        return root
    elif left:
        return left
    else:
        return right

# O(N)
def LCA_2(root: TreeNode, p: TreeNode, q: TreeNode):
    def print_path(path, current, target):
        if not current:
            return path

        path.append(current)
        if current == target:
            return path

        if current.left:
            left_path = print_path(path, current.left, target)
            if left_path[-1] == target:
                return left_path
        if current.right:
            right_path = print_path(path, current.right, target)
            if right_path[-1] == target:
                return right_path
        return path

    path_p = print_path([], root, p)
    path_q = print_path([], root, q)
    for i in range(min(len(path_p), len(path_q))):
        if path_p[i] != path_q[i]:
            return path_p[i - 1]

    if len(path_p) < len(path_q):
        return path_p[-1]
    else:
        return path_q[-1]

# Pre-processing O(NlogN), query O(logN), Binary lifting
# Support searching k-th parent node, also support new node insertion
# Store 2^i-th ancestor for every node
def LCA_3(root: TreeNode):
    bl = {}
    N = len(edge)
    K = int(math.log2(N+1)) + 1 # Max depth of the binary lifting
    

    def query(p: TreeNode, q: TreeNode):
