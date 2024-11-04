# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# iteration
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []

        result = []
        current_level = [root]
        while current_level:
            next_level = []
            current_level_val = []
            for node in current_level:
                current_level_val.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            result.append(current_level_val)
            current_level = next_level
        return result

# recursion
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []

        left_level_order = self.levelOrder(root.left)
        right_level_order = self.levelOrder(root.right)
        leftN = len(left_level_order)
        rightN = len(right_level_order)

        result = [[] for _ in range(max(leftN, rightN) + 1)]
        result[0].append(root.val)
        for i in range(leftN):
            result[i + 1].extend(left_level_order[i])
        for i in range(rightN):
            result[i + 1].extend(right_level_order[i])

        return result
