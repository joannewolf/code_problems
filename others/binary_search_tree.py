class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



def traverseBST(root):
    stack = []
    current = root
    while current or stack:
        while current:
            stack.append(current)
            current = current.left

        current = stack.pop()
        print(current.val)
        current = current.right

nums = [5,1,4,None,None,3,6]
