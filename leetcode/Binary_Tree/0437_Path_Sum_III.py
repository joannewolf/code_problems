# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findPathSum(self, prefixSum, root, targetSum):
        if not root:
            return 0

        for sum in prefixSum:
            if sum + root.val == targetSum:
                self.count += 1

        if root.val == targetSum:
            self.count += 1

        newPrefixSum = [sum + root.val for sum in prefixSum] + [root.val]
        self.findPathSum(newPrefixSum, root.left, targetSum)
        self.findPathSum(newPrefixSum, root.right, targetSum)

    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: int
        """
        self.count = 0
        self.findPathSum([], root, targetSum)
        return self.count
