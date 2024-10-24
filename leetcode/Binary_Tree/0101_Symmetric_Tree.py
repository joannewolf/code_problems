# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# recursion
class Solution(object):
    def isSymmetricNode(self, left, right):
        if not left and not right:
            return True
        if not left and right:
            return False
        if left and not right:
            return False
        if left.val != right.val:
            return False
        
        return self.isSymmetricNode(left.left, right.right) & self.isSymmetricNode(left.right, right.left)

    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if not root:
            return True

        return self.isSymmetricNode(root.left, root.right)

# iteration
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if not root:
            return True

        left_nodes = [root.left]
        right_nodes = [root.right]
        while left_nodes and right_nodes:
            left = left_nodes.pop(0)
            right = right_nodes.pop(0)
            if not left and not right:
                pass
            elif not left and right:
                return False
            elif left and not right:
                return False
            elif left.val != right.val:
                return False
            else:
                left_nodes.append(left.left)
                left_nodes.append(left.right)
                right_nodes.append(right.right)
                right_nodes.append(right.left)

        return True
