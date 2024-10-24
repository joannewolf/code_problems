# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# iteration
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        current_layer_p = [p]
        current_layer_q = [q]
        while current_layer_p and current_layer_q:
            next_layer_p = []
            next_layer_q = []
            for i in range(len(current_layer_p)):
                if not current_layer_p[i] and not current_layer_q[i]:
                    pass
                elif current_layer_p[i] and not current_layer_q[i]:
                    return False
                elif not current_layer_p[i] and current_layer_q[i]:
                    return False
                else:
                    if current_layer_p[i].val != current_layer_q[i].val:
                        return False
                    next_layer_p.append(current_layer_p[i].left)
                    next_layer_p.append(current_layer_p[i].right)
                    next_layer_q.append(current_layer_q[i].left)
                    next_layer_q.append(current_layer_q[i].right)

            current_layer_p = next_layer_p
            current_layer_q = next_layer_q

        if current_layer_p or current_layer_q:
            return False

        return True

# recursion
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """

        if not p and not q:
            return True
        elif not p and q:
            return False
        elif p and not q:
            return False
        else:
            if p.val != q.val:
                return False
            else:
                return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
