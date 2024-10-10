class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for char in s:
            if char in ['(', '[', '{']:
                stack.append(char)
            elif char == ')':
                if not stack or stack[-1] != '(':
                    return False
                else:
                    stack.pop()
            elif char == ']':
                if not stack or stack[-1] != '[':
                    return False
                else:
                    stack.pop()
            elif char == '}':
                if not stack or stack[-1] != '{':
                    return False
                else:
                    stack.pop()

        return False if stack else True
