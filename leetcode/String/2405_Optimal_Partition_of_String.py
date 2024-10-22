class Solution(object):
    def partitionString(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0

        # greedily add char until duplicate
        dict = set()
        for char in s:
            if char not in dict:
                dict.add(char)
            else:
                count += 1
                dict.clear()
                dict.add(char)

        return count + 1 # 1 for last partition
