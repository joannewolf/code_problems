class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        flowerbed = [0] + flowerbed + [0, 1] # last 1 for trigger add last zero_count to result
        N = len(flowerbed)
        count = 0

        zero_count = 0
        for i in range(N):
            if flowerbed[i] == 0:
                zero_count += 1
            else:
                count += (zero_count - 1) // 2
                zero_count = 0

        return (count >= n)
