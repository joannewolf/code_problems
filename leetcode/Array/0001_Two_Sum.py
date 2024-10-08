# O(N^2)
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        N = len(nums)
        for i in range(N):
            for j in range(i+1, N):
                if nums[i] + nums[j] == target:
                    return [i, j]

# O(NlogN)
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums = list(enumerate(nums)) # convert list to [(index, value)] list
        nums.sort(key=lambda x: x[1]) # sort by value
        N = len(nums)
        i, j = 0, N - 1
        while True:
            if nums[i][1] + nums[j][1] > target:
                j -= 1
            elif nums[i][1] + nums[j][1] < target:
                i += 1
            else:
                return [nums[i][0], nums[j][0]]

# O(N)
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        index_map = {} # index_map[value] = index
        N = len(nums)
        for i in range(N):
            if (target - nums[i]) in index_map:
                return [index_map[target - nums[i]], i]
            else:
                index_map[nums[i]] = i
