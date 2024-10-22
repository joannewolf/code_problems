class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s

        N = len(s)
        rows = [''] * numRows
        current_row = 0
        direction = 1
        for i in range(N):
            rows[current_row] += s[i]
            current_row += direction
            if current_row == numRows - 1:
                direction = -1
            elif current_row == 0:
                direction = 1

        result = ''
        for i in range(numRows):
            result += rows[i]
        
        return result
