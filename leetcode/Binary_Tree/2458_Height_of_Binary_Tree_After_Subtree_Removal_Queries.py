# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getHeight(self, root):
        if not root:
            return 0

        height = max(self.getHeight(root.left), self.getHeight(root.right)) + 1
        self.heights[root.val] = height - 1 # only count the edge, not node
        return height

    def treeQueries(self, root, queries):
        """
        :type root: Optional[TreeNode]
        :type queries: List[int]
        :rtype: List[int]
        """
        self.heights = {} # heights[i] means the subtree height at val i
        ans = {} # ans[i] means the tree height after removing subtree at val i

        self.getHeight(root)
        # BFS, ans[i] = current depth + max height of same depth subtrees except subtree i)
        depth = 0
        current_layer = [root]
        while current_layer:
            next_layer = []
            current_heights = [self.heights[node.val] for node in current_layer]
            current_heights.sort(reverse=True)
            for node in current_layer:
                if self.heights[node.val] != current_heights[0]: # not the highest subtree
                    ans[node.val] = depth + current_heights[0]
                else: # is the highest subtree
                    if len(current_heights) == 1:
                        ans[node.val] = depth - 1 # remove the one and only subtree
                    else:
                        ans[node.val] = depth + current_heights[1]

                if node.left:
                    next_layer.append(node.left)
                if node.right:
                    next_layer.append(node.right)

            depth += 1
            current_layer = next_layer

        return [ans[i] for i in queries]
