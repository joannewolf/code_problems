class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [0] + nums + [0, -1]
        # count 0, 1, ..., 0 in nums
        counts = []
        count = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                count += 1
            else:
                counts.append(count)
                count = 1
        counts[0] -= 1
        counts[-1] -= 1

        N = len(counts)
        print(counts)
        if N == 3 and counts[0] == 0 and counts[-1] == 0:
            # all 1's
            return counts[1] - 1
        else:
            max_count = 0
            for i in range(1, N, 2):
                # if removing any 0
                max_count = max(max_count, counts[i])
                # if only one 0 between two 1's
                if i >= 3 and counts[i - 1] == 1:
                    max_count = max(max_count, counts[i - 2] + counts[i])

            return max_count
