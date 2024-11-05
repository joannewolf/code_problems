class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        N = len(tokens)
        stack = []
        for i in range(N):
            if tokens[i] not in ['+', '-', '*', '/']:
                stack.append(int(tokens[i]))
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                if tokens[i] == '+':
                    stack.append(num1 + num2)
                elif tokens[i] == '-':
                    stack.append(num1 - num2)
                elif tokens[i] == '*':
                    stack.append(num1 * num2)
                elif tokens[i] == '/':
                    sign = -1 if (num1 < 0) ^ (num2 < 0) else 1
                    stack.append(abs(num1) // abs(num2) * sign)

        return stack[0]
