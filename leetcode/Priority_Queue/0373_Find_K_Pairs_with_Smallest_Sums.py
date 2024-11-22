class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        N, M = len(nums1), len(nums2)
        # for each num in nums1, record the current index of corresponding num in nums2
        # and maintain by non-decreasing sum val
        pq = [(nums1[i] + nums2[0], i, 0) for i in range(N)] # list of tuple (sum val, nums1 index, nums2 index)
        result = []
        for _ in range(k):
            _, i, j = pq.pop(0)
            result.append([nums1[i], nums2[j]])
            if j == M - 1:
                continue
            else:
                new_tuple = (nums1[i] + nums2[j+1], i, j+1)
                # use binary search to insert new tuple back to pq
                left, right = 0, len(pq) - 1
                while left <= right:
                    mid = (left + right) // 2
                    if pq[mid][0] <= new_tuple[0]:
                        left = mid + 1
                    else:
                        right = mid - 1
                # final L is min element index which > target, i.e. inserting point
                pq.insert(left, new_tuple)

        return result
