# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def DFS(self, root, leafs):
        if not root:
            return
        if not root.left and not root.right: # lead node
            leafs.append(root.val)
            return

        if root.left:
            self.DFS(root.left, leafs)
        if root.right:
            self.DFS(root.right, leafs)

    def leafSimilar(self, root1, root2):
        """
        :type root1: Optional[TreeNode]
        :type root2: Optional[TreeNode]
        :rtype: bool
        """
        leaf1 = []
        leaf2 = []
        self.DFS(root1, leaf1)
        self.DFS(root2, leaf2)

        return (leaf1 == leaf2)
