class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        num_set1 = set(nums1)
        num_set2 = set(nums2)
        diff1 = set()
        diff2 = set()
        for num in nums1:
            if num not in num_set2:
                diff1.add(num)
        for num in nums2:
            if num not in num_set1:
                diff2.add(num)

        return [list(diff1), list(diff2)]
