class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s += '.' # for triggering last calculation
        self.stack_num = [0]
        self.stack_sign = [1] # last sign is for the next number
        self.num_str = ''

        def mergeLastNum():
            if self.num_str:
                last_num = self.stack_sign.pop() * int(self.num_str)
                self.stack_num[-1] += last_num
                self.num_str = ''
            else:
                # if prev is ')', replace the temp '+'
                # if prev is '(' and next sign is '-', replace the initial '+'
                self.stack_sign.pop()

        for char in s:
            if char.isdigit():
                self.num_str += char
            elif char == '+':
                mergeLastNum()
                self.stack_sign.append(1)
            elif char == '-':
                mergeLastNum()
                self.stack_sign.append(-1)
            elif char == '(':
                self.stack_num.append(0)
                self.stack_sign.append(1) # initial with '+'
            elif char == ')':
                mergeLastNum()
                last_num = self.stack_sign.pop() * self.stack_num.pop()
                self.stack_num[-1] += last_num
                self.stack_sign.append(1) # not sure next sign, so giving temp '+'
            elif char == '.':
                mergeLastNum()
            else:
                pass

        return self.stack_num[0]