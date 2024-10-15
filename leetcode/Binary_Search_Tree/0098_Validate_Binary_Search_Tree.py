# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# recursion
class Solution(object):
    def validNode(self, node, min_val, max_val):
        if not node:
            return True
        if node.val <= min_val or node.val >= max_val:
            return False

        return (self.validNode(node.left, min_val, node.val) and self.validNode(node.right, node.val, max_val))

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        INT_MIN = -pow(2, 31) - 1
        INT_MAX = pow(2, 31)
        return self.validNode(root, INT_MIN, INT_MAX)

# iteration, traverse in order should get increasing nums
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        stack = []
        current, prev = root, None
        while current or stack:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            if prev and prev.val >= current.val:
                return False
            prev = current
            current = current.right

        return True
