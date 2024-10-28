# O(1) space with division
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        N = len(nums)
        zero_index = []
        product = 1
        for i in range(N):
            if nums[i] == 0:
                zero_index.append(i)
            else:
                product *= nums[i]

        if len(zero_index) > 1:
            return [0] * N
        elif len(zero_index) == 1:
            result = [0] * N
            result[zero_index[0]] = product
            return result
        else:
            result = [product // num for num in nums]
            return result

# O(1) space without division
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        N = len(nums)
        # result[i] = product of nums[0:i] * product of nums[i+1:N]
        result = [1] * N

        # add left half product
        temp = 1
        for i in range(N):
            result[i] *= temp
            temp *= nums[i]
        # add right half product
        temp = 1
        for i in range(N - 1, -1, -1):
            result[i] *= temp
            temp *= nums[i]

        return result
