class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []

        N = len(nums)
        start, end = nums[0], nums[0]
        result = []
        for i in range(1, N):
            if nums[i] == end + 1:
                end = nums[i]
            else:
                if start != end:
                    result.append(str(start) + '->' + str(end))
                else:
                    result.append(str(start))

                start, end = nums[i], nums[i]

        if start != end:
            result.append(str(start) + '->' + str(end))
        else:
            result.append(str(start))
        return result
