# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        self._push_all(root)

    def _push_all(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    # return next smallest num
    def next(self):
        """
        :rtype: int
        """
        current = self.stack.pop()
        self._push_all(current.right)
        return current.val

    def hasNext(self):
        """
        :rtype: bool
        """
        return bool(self.stack)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
