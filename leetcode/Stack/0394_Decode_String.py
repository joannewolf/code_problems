class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        repeat = []
        stack = ['']
        num = ''
        for char in s:
            if char.isdigit():
                num += char
            elif char.isalpha():
                stack[-1] += char
            elif char == '[':
                repeat.append(int(num))
                num = ''
                stack.append('')
            elif char == ']':
                last_repeat = repeat.pop()
                last_str = stack.pop()
                stack[-1] += last_repeat * last_str

        return stack[0]
