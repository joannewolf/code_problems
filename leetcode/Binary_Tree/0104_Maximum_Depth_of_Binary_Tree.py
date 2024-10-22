# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# iteration
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0

        layer = 0
        current_layer = [root]
        while current_layer:
            layer += 1
            next_layer = []
            for node in current_layer:
                if node.left:
                    next_layer.append(node.left)
                if node.right:
                    next_layer.append(node.right)

            current_layer = next_layer

        return layer

# recurrsion
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0

        result = 1
        if root.left:
            result = max(result, self.maxDepth(root.left) + 1)
        if root.right:
            result = max(result, self.maxDepth(root.right) + 1)

        return result
