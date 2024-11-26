class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_set = set(nums)
        max_len = 0
        for num in num_set:
            if num - 1 in num_set:
                continue
            else:
                count = 0
                current_num = num
                while True:
                    if current_num in num_set:
                        count += 1
                        current_num += 1
                    else:
                        break
                max_len = max(max_len, count)

        return max_len
