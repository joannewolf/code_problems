class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        num_set = set()
        num_set.add(n)

        while True:
            sum = 0
            while n != 0:
                sum += (n % 10) * (n % 10)
                n //= 10
            
            if sum == 1:
                return True
            elif sum in num_set:
                return False
            else:
                num_set.add(sum)
                n = sum
