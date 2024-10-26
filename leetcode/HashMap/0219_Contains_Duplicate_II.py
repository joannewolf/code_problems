class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        N = len(nums)
        index_dict = {}
        for i, num in enumerate(nums):
            if num not in index_dict:
                index_dict[num] = i
            else:
                if i - index_dict[num] <= k:
                    return True
                else:
                    index_dict[num] = i

        return False
