class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        zero_count = 0
        num_set = set()
        for num in arr:
            if num == 0:
                zero_count += 1
            else:
                num_set.add(num)

        if zero_count >= 2:
            return True

        for num in num_set:
            if num * 2 in num_set:
                return True

        return False
