# Same as 783
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        INT_MAX = 1000000
        min_diff = INT_MAX
        # traverse in-order to get diff
        stack = []
        current, prev = root, None
        while current or stack:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            if prev and current.val - prev.val < min_diff:
                min_diff = current.val - prev.val
            prev = current
            current = current.right

        return min_diff
