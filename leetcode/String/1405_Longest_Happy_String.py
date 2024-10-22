class Solution(object):
    def longestDiverseString(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: str
        """
        result = ''
        # greedily put the char with max num and not break the rule
        while True:
            next = ''
            if result[-2:] == 'aa':
                if b > 0 and b == max(b, c):
                    next = 'b'
                elif c > 0 and c == max(b, c):
                    next = 'c'
            elif result[-2:] == 'bb':
                if a > 0 and a == max(a, c):
                    next = 'a'
                elif c > 0 and c == max(a, c):
                    next = 'c'
            elif result[-2:] == 'cc':
                if a > 0 and a == max(a, b):
                    next = 'a'
                elif b > 0 and b == max(a, b):
                    next = 'b'
            else:
                if a > 0 and a == max(a, b, c):
                    next = 'a'
                elif b > 0 and b == max(a, b, c):
                    next = 'b'
                elif c > 0 and c == max(a, b, c):
                    next = 'c'

            if not next:
                break
            else:
                result += next
                if next == 'a':
                    a -= 1
                elif next == 'b':
                    b -= 1
                elif next == 'c':
                    c -= 1

        return result
