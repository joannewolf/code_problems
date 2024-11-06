# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findPathSum(self, prefix, node, targetSum):
        if not node:
            return

        if not node.left and not node.right:
            if sum(prefix) + node.val == targetSum:
                self.result.append(prefix + [node.val])

        new_prefix = prefix + [node.val]
        self.findPathSum(new_prefix, node.left, targetSum)
        self.findPathSum(new_prefix, node.right, targetSum)

    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: List[List[int]]
        """
        self.result = []
        self.findPathSum([], root, targetSum)

        return self.result
