class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result = [0, 1]

        while True:
            next_bits = [count + 1 for count in result]
            result += next_bits

            if len(result) > n + 1:
                break
        
        return result[:n + 1]
