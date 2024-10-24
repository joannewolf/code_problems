# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# DFS
class Solution(object):
    def getPath(self, node, val):
        if not node:
            return None
        if node.val == val:
            return [val]

        left_path = self.getPath(node.left, val)
        if left_path:
            left_path.insert(0, node.val)
            return left_path
        right_path = self.getPath(node.right, val)
        if right_path:
            right_path.insert(0, node.val)
            return right_path

    def isCousins(self, root, x, y):
        """
        :type root: Optional[TreeNode]
        :type x: int
        :type y: int
        :rtype: bool
        """
        x_path = self.getPath(root, x)
        y_path = self.getPath(root, y)

        if len(x_path) != len(y_path):
            return False
        N = len(x_path)
        if x_path[N - 2] == y_path[N - 2]:
            return False
        else:
            return True
