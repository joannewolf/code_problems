# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def reverseOddLevels(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if not root:
            return root

        current_layer = 0
        current_nodes = [root]
        while current_nodes:
            if current_layer % 2 == 1:
                node_vals = [node.val for node in current_nodes]
                node_vals.reverse()
                for i, node in enumerate(current_nodes):
                    node.val = node_vals[i]

            next_nodes = []
            if current_nodes[0].left:
                for node in current_nodes:
                    next_nodes.append(node.left)
                    next_nodes.append(node.right)
            current_nodes = next_nodes
            current_layer += 1

        return root
