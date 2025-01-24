# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def largestValues(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if not root:
            return []

        result = []
        current_layer = [root]
        while current_layer:
            next_layer = []
            max_val = max([node.val for node in current_layer])
            result.append(max_val)

            for node in current_layer:
                if node.left:
                    next_layer.append(node.left)
                if node.right:
                    next_layer.append(node.right)

            current_layer = next_layer

        return result
