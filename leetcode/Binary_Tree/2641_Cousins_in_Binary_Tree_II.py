# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def replaceValueInTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if not root:
            return root

        current_layer = [root]
        current_layer_sum = root.val
        root.val = -root.val

        while current_layer:
            next_layer = []
            next_layer_sum = 0
            for node in current_layer:
                node.val += current_layer_sum
                # update child node val with negative siblings sum
                sibling_sum = 0
                if node.left:
                    sibling_sum += node.left.val
                    next_layer_sum += node.left.val
                    next_layer.append(node.left)
                if node.right:
                    sibling_sum += node.right.val
                    next_layer_sum += node.right.val
                    next_layer.append(node.right)

                if node.left:
                    node.left.val = -sibling_sum
                if node.right:
                    node.right.val = -sibling_sum

            current_layer = next_layer
            current_layer_sum = next_layer_sum

        return root
