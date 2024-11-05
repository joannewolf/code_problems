# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def DFS(self, root, num_str):
        if not root.left and not root.right:
            num_str += str(root.val)
            self.result += int(num_str)
            return

        if root.left:
            self.DFS(root.left, num_str + str(root.val))
        if root.right:
            self.DFS(root.right, num_str + str(root.val))

    def sumNumbers(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.result = 0
        self.DFS(root, '')

        return self.result
