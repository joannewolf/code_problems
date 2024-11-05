class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        dirs = path.split('/')
        stack = []
        for dir in dirs:
            if not dir or dir == '.':
                pass
            elif dir == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(dir)

        return '/' + '/'.join(stack)
