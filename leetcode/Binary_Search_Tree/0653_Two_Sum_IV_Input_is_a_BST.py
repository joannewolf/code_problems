# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        if not root:
            return False

        nums = set()
        # add all nums in set
        queue = [root] # node in queue must have val
        while queue:
            current = queue.pop(0)
            if k - current.val in nums:
                return True
            else:
                nums.add(current.val)

            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
