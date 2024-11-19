class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        for _ in range(n):
            nums1.pop()
        i, j = 0, 0
        while j < n:
            if i == len(nums1):
                nums1.append(nums2[j])
                j += 1
            elif nums1[i] <= nums2[j]:
                i += 1
            else:
                nums1.insert(i, nums2[j])
                i += 1
                j += 1
