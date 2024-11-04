# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[float]
        """

        result = []
        current_level = [root]
        while current_level:
            node_sum = 0
            next_level = []
            for node in current_level:
                node_sum += node.val
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            result.append(float(node_sum) / len(current_level))
            current_level = next_level

        return result
