# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flipEquiv(self, root1, root2):
        """
        :type root1: Optional[TreeNode]
        :type root2: Optional[TreeNode]
        :rtype: bool
        """
        if not root1 and not root2:
            return True
        if not root1 and root2:
            return False
        if root1 and not root2:
            return False
        if root1.val != root2.val:
            return False

        left1 = root1.left
        right1 = root1.right
        child_vals1 = set()
        left2 = root2.left
        right2 = root2.right
        child_vals2 = set()
        if left1:
            child_vals1.add(left1.val)
        if right1:
            child_vals1.add(right1.val)
        if left2:
            child_vals2.add(left2.val)
        if right2:
            child_vals2.add(right2.val)

        if child_vals1 != child_vals2:
            return False
        N = len(child_vals1)
        if N == 0:
            return True
        if N == 1:
            if left1:
                new_root1 = left1
            if right1:
                new_root1 = right1
            if left2:
                new_root2 = left2
            if right2:
                new_root2 = right2
            return self.flipEquiv(new_root1, new_root2)
        if N == 2:
            if left1.val == left2.val:
                return self.flipEquiv(left1, left2) & self.flipEquiv(right1, right2)
            else:
                return self.flipEquiv(left1, right2) & self.flipEquiv(right1, left2)
