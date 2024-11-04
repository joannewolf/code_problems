# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0

        result = 0
        current_level = [root]
        current_level_node_count = 1
        while current_level:
            result += current_level_node_count
            next_level = []

            if current_level[-1].right:
                for node in current_level:
                    next_level.append(node.left)
                    next_level.append(node.right)

                current_level = next_level
                current_level_node_count *= 2
            else: # only possible incomplete in leaf level
                for node in current_level:
                    if node.left:
                        result += 1
                    else:
                        break
                    if node.right:
                        result += 1
                    else:
                        break

                break

        return result
